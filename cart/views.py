from django.shortcuts import render, redirect, get_object_or_404, redirect
from product_catalog.models import Product, ProductVariant


def cart_detail(request):
    """ A view that renders the cart contents"""

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    # Get the product by ID
    product = get_object_or_404(Product, id=item_id)

    # Handle the case if there are variants
    variant_id = request.POST.get('variant')
    quantity = int(request.POST.get('quantity', 1))  # Default quantity to 1 

    # Check if variant is selected and exists
    if variant_id:
        variant = get_object_or_404(ProductVariant, id=variant_id)
        price = variant.price
    else:
        variant = None
        price = product.price

    # Get the current cart session
    cart = request.session.get('cart', {})

    # If variant exists, use variant ID, otherwise use product ID
    key = variant_id if variant else str(item_id)

    # Check if the product/variant is already in the cart
    if key in cart:
        # Ensure cart[key] is a dictionary before trying to access its 'quantity' key
        if isinstance(cart[key], dict):
            # Increment the quantity if the product/variant is already in the cart
            cart[key]['quantity'] += quantity
        else:
            # If it's not a dictionary, reinitialize it properly
            cart[key] = {
                'product_id': product.id,
                'variant_id': variant.id if variant else None,
                'quantity': quantity,
                'price': str(price)
            }
    else:
        # Add the product/variant to the cart as a dictionary
        cart[key] = {
            'product_id': product.id,
            'variant_id': variant.id if variant else None,
            'quantity': quantity,
            'price': str(price)
        }

    # Save the updated cart back to the session
    request.session['cart'] = cart

    # Redirect to the specified URL
    redirect_url = request.POST.get('redirect_url', '/')
    return redirect(redirect_url)
