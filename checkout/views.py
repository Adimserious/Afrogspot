from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CheckoutForm
from .models import Order, OrderItem, Product, ProductVariant
from decimal import Decimal
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    # Get the cart from session
    cart = request.session.get('cart', {})

    # Check if cart is empty
    if not cart:
        messages.error(request, 'Your cart is empty. Please add items to your cart before proceeding to checkout.')
        return redirect('cart_detail')

    # Calculate order total
    order_total = calculate_order_total(request)
    delivery_cost = Decimal('7.00')  # Example delivery cost
    grand_total = order_total + delivery_cost

    # Create PaymentIntent
    try:
        intent = stripe.PaymentIntent.create(
            amount=int(grand_total * 100),  # Convert to cents
            currency='eur',
        )
        client_secret = intent.client_secret
    except stripe.error.StripeError as e:
        messages.error(request, f'Error with Stripe: {str(e)}')
        return redirect('cart_detail')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # The payment has been confirmed client-side; create the order
            order = form.save(commit=False)
            order.user = request.user if request.user.is_authenticated else None
            order.order_total = order_total
            order.delivery_cost = delivery_cost
            order.grand_total = grand_total
            order.save()

            # Create order items
            for key, item_data in cart.items():
                if isinstance(item_data, dict):
                    product = get_object_or_404(Product, id=item_data['product_id'])
                    variant = None
                    if item_data.get('variant_id'):
                        variant = get_object_or_404(ProductVariant, id=item_data['variant_id'])
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        variant=variant,
                        quantity=item_data['quantity'],
                        price=Decimal(item_data['price'])
                    )

            # Clear the cart
            request.session['cart'] = {}

            # Saves user info if `save_info` is checked
            save_info = 'save_info' in request.POST
            if save_info and request.user.is_authenticated:
                profile = request.user.profile
                profile.full_name = form.cleaned_data['full_name']
                profile.email = form.cleaned_data['email']
                profile.phone_number = form.cleaned_data['phone_number']
                profile.address_line_1 = form.cleaned_data['address_line_1']
                profile.address_line_2 = form.cleaned_data['address_line_2']
                profile.city = form.cleaned_data['city']
                profile.postal_code = form.cleaned_data['postal_code']
                profile.country = form.cleaned_data['country']
                profile.save()

            messages.success(request, 'Your order has been placed successfully!')
            return redirect('order_confirmation', order_id=order.id)
    else:
        form = CheckoutForm()

    context = {
        'form': form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': client_secret,
        'order_total': order_total,
        'delivery_cost': delivery_cost,
        'grand_total': grand_total,
    }

    return render(request, 'checkout/checkout.html', context)

def calculate_order_total(request):
    cart = request.session.get('cart', {})
    total = Decimal(0)
    for item_data in cart.values():
        if isinstance(item_data, dict):
            price = Decimal(item_data['price'])
            quantity = item_data['quantity']
            total += price * quantity
    return total

def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'checkout/order_confirmation.html', {'order': order})


@login_required
def order_history(request):
    # Filter orders for the current user
    orders = Order.objects.filter(user=request.user).order_by('-date_ordered')
    return render(request, 'order_history.html', {'orders': orders})