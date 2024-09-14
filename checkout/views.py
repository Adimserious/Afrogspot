from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CheckoutForm
from .models import Order, OrderItem, OrderItem
from decimal import Decimal


def checkout(request):
    # Get the cart from session, default to an empty dictionary
    cart = request.session.get('cart', {})

    # Check if cart is empty
    if not cart:
        messages.error(request, 'Your cart is empty. Please add items to your cart before proceeding to checkout.')
        return redirect('cart_detail')  # Redirect to the cart page

    # checkout process
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Creates the order
            order = form.save(commit=False)
            order.user = request.user if request.user.is_authenticated else None
            order.order_total = calculate_order_total(request)  # Custom function to calculate total
            order.grand_total = order.order_total + order.delivery_cost
            order.save()

            # Creates order items
            cart = request.session.get('cart', {})
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
            
            # If user checked the checkbox, save address to their profile
            if save_info:
                request.user.profile.full_name = full_name
                request.user.profile.address_line_1 = address_line_1
                # Other profile fields...
                request.user.profile.save()

            # Show success message
            messages.success(request, 'Your order has been placed successfully!')
            return redirect('order_confirmation', order_id=order.id)
    else:
        form = CheckoutForm()

    return render(request, 'checkout/checkout.html', {'form': form})


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
