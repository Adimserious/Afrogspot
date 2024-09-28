from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CheckoutForm
from profiles.forms import ProfileForm
from profiles.models import Profile
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

    # Condition to determine if free delivery should be applied
    free_delivery_threshold = 50  # Free delivery on orders above €50
    if order_total >= free_delivery_threshold:
        delivery_cost = Decimal('0.00')  # Free delivery
    else:
        delivery_cost = Decimal('7.00')  # Standard delivery cost

    grand_total = order_total + delivery_cost

    # Creates PaymentIntent
    try:
        intent = stripe.PaymentIntent.create(
            amount=int(grand_total * 100),  # Convert to cents
            currency='eur',
        )
        #print(intent)   
        client_secret = intent.client_secret
    except stripe.error.StripeError as e:
        messages.error(request, f'Error with Stripe: {str(e)}')
        return redirect('cart_detail') 

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # The payment has been confirmed on the client-side; creates the order
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
            save_info = form.cleaned_data.get('save_info')
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

            # Order confirmation email
            send_order_confirmation_email(order)

            messages.success(request, 'Your order has been placed successfully!')
            return redirect('order_confirmation', order_id=order.id)
    else:
        # If the user is authenticated, prefill the form with their profile information
        if request.user.is_authenticated:
            profile = request.user.profile
            initial_data = {
                'full_name': profile.default_full_name,
                'email': profile.default_email,
                'phone_number': profile.default_phone_number,
                'address_line_1': profile.default_address_line_1,
                'address_line_2': profile.default_address_line_2,
                'city': profile.default_city,
                'postal_code': profile.default_postal_code,
                'country': profile.default_country,
            }
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


def send_order_confirmation_email(order):
    subject = f'Order Confirmation - Order #{order.id}'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [order.email]

    # Renders the HTML email content using a template
    html_message = render_to_string('checkout/order_email_confirmation.html', {'order': order})
    plain_message = strip_tags(html_message)

    # Sends the email
    send_mail(
        subject,
        plain_message,
        from_email,
        to_email,
        html_message=html_message,
        fail_silently=False,
    )


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
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'checkout/order_confirmation.html', {'order': order})


@login_required
def order_history(request):
    # Retrieve orders for the current user
    orders = Order.objects.filter(user=request.user).order_by('-date_ordered')
    
    context = {
        'orders': orders,
    }
    return render(request, 'checkout/order_history.html', context)


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.filter(order=order)

    # Pass total calculation to context
    for item in order_items:
        item.total_price = item.price * item.quantity

    context = {
        'order': order,
        'order_items': order_items,
        'delivery_cost': order.delivery_cost,  # Adds delivery cost
        'grand_total': order.grand_total,      # Adds grand total
    }
    return render(request, 'checkout/order_detail.html', context)