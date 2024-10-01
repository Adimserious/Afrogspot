from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from product_catalog.models import Product, ProductVariant
from django.conf import settings




def cart_detail(request):
    # Get the cart from session, default to an empty dictionary
    cart = request.session.get('cart', {})
    
    cart_items = []
    
    # Iterate over the cart dictionary
    for key, item_data in cart.items():
        # Ensures that item_data is a dictionary
        if not isinstance(item_data, dict):
            continue  # Skips this item if item_data is not a dictionary
        
        # Checks that the product_id exists in item_data
        if 'product_id' not in item_data:
            continue  # Skips if the data is malformed
        
        # Gets the product from the database
        product = get_object_or_404(Product, id=item_data['product_id'])
        
        # Creates the cart item dictionary
        item = {
            'item_id': key,  # The key is either product or variant ID
            'product': product,
            'quantity': item_data['quantity'],
            'price': float(item_data['price']),
            'total_price': float(item_data['quantity']) * float(item_data['price']),
        }

        # Check if a variant exists
        if item_data.get('variant_id'):
            variant = get_object_or_404(ProductVariant, id=item_data['variant_id'])
            item['variant'] = variant  # Add variant info to item

        # Appends the item to the cart_items list
        cart_items.append(item)

    # Calculates total cart price
    total = sum(item['total_price'] for item in cart_items)

    # free shipping threshold 
    free_shipping_threshold = getattr(settings, 'FREE_SHIPPING_THRESHOLD', 50)

    # Determines if the cart is eligible for free shipping
    eligible_for_free_shipping = total >= free_shipping_threshold

    # Calculate amount needed for free shipping
    #amount_needed_for_free_shipping = max(0, free_shipping_threshold - total)

    context = {
        'cart_items': cart_items,
        'total': total,
        'free_shipping_threshold': free_shipping_threshold,
        'eligible_for_free_shipping': eligible_for_free_shipping,
    }

    return render(request, 'cart/cart.html', context)



def add_to_cart(request, item_id):
    # Get the product by ID
    product = get_object_or_404(Product, id=item_id)

    # Handles the case if there are variants
    variant_id = request.POST.get('variant')
    quantity = int(request.POST.get('quantity', 1))  # Default quantity to 1


    # Checks if variant is selected and exists
    if variant_id:
        variant = get_object_or_404(ProductVariant, id=variant_id)
        price = variant.price
        stock = variant.stock
        # Use both product and variant ID to create a unique key
        key = f"{item_id}-{variant_id}"
    else:
        variant = None
        price = product.price
        stock = product.stock
        # Use just the product ID for the key if no variant exists
        key = str(item_id)

    # Check if the quantity requested exceeds available stock
    if stock < quantity:
        messages.error(request, f'Sorry, only {stock} of {variant.size} kg of {product.name} are available.')
        return redirect(request.POST.get('redirect_url', '/'))

    # Gets the current cart session
    cart = request.session.get('cart', {})

    # Checks if the product/variant is already in the cart
    if key in cart:
        # Increment the quantity if the product/variant is already in the cart
        cart[key]['quantity'] += quantity
        messages.success(request, f'Updated quantity for {product.name} in your cart!')
    else:
        # Adds the product/variant to the cart as a dictionary
        cart[key] = {
            'product_id': product.id,
            'variant_id': variant.id if variant else None,
            'quantity': quantity,
            'price': str(price)
        }
        messages.success(request, f'{product.name} added to your cart!')

    # Saves the updated cart back to the session
    request.session['cart'] = cart

    # Redirect to the specified URL
    redirect_url = request.POST.get('redirect_url', '/')
    return redirect(redirect_url)


def update_cart_quantity(request, item_id):
    """Updates the quantity of a cart item via form submission."""
    if request.method == 'POST':
        # Get the quantity from the form
        quantity = int(request.POST.get('quantity', 1))

        # Get the current cart session
        cart = request.session.get('cart', {})

        # Ensures that the item exists in the cart
        if item_id in cart:
            # Check the current item details
            item_data = cart[item_id]
            product = get_object_or_404(Product, id=item_data['product_id'])
            variant = None
            
            if item_data.get('variant_id'):
                variant = get_object_or_404(ProductVariant, id=item_data['variant_id'])

            # Validate the quantity against stock
            if quantity > 0:
                if variant and quantity > variant.stock:
                    messages.error(request, f'Sorry, only {variant.stock} of {variant.size} kg of {product.name} are available.')
                elif quantity > product.stock:
                    messages.error(request, f'Sorry, only {product.stock} of {product.name} are available.')
                else:
                    cart[item_id]['quantity'] = quantity
                    messages.success(request, 'Item quantity updated in your cart!')
            else:
                # Remove the item if the quantity is 0
                del cart[item_id]
                messages.success(request, 'Item removed from your cart!')

        # Save the updated cart back to the session
        request.session['cart'] = cart

        # Redirect back to the cart page
        return redirect('cart_detail')

    # If the request is not POST, redirect to the cart page
    return redirect('cart_detail')


def remove_from_cart(request, item_id):
    """Removes an item from the cart."""
    cart = request.session.get('cart', {})

    # Ensures the item exists in the cart before trying to remove it
    if str(item_id) in cart:
        item_data = cart[str(item_id)]
        product = get_object_or_404(Product, id=item_data['product_id'])
        variant = None
        
        if item_data.get('variant_id'):
            variant = get_object_or_404(ProductVariant, id=item_data['variant_id'])

        del cart[str(item_id)]
        if variant:
            messages.success(request, f'{variant.size} kg of {product.name} removed from your cart!')
        else:
            messages.success(request, f'{product.name} removed from your cart!')

    # Save the updated cart back to the session
    request.session['cart'] = cart

    # Redirect to the cart detail page
    return redirect('cart_detail')
