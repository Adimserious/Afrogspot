from django.shortcuts import render, redirect, get_object_or_404, redirect
from product_catalog.models import Product, ProductVariant



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

        # Checks if a variant exists
        if item_data.get('variant_id'):
            item['variant'] = get_object_or_404(ProductVariant, id=item_data['variant_id'])
        
        # Appends the item to the cart_items list
        cart_items.append(item)

    # Calculates total cart price
    total = sum(item['total_price'] for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total': total,
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
    else:
        variant = None
        price = product.price

    # Gets the current cart session
    cart = request.session.get('cart', {})

    # If variant exists, use variant ID, otherwise use product ID
    key = variant_id if variant else str(item_id)

    # Checks if the product/variant is already in the cart
    if key in cart:
        if isinstance(cart[key], dict):
            # Increment the quantity if the product/variant is already in the cart
            cart[key]['quantity'] += quantity
        else:
            cart[key] = {
                'product_id': product.id,
                'variant_id': variant.id if variant else None,
                'quantity': quantity,
                'price': str(price)
            }
    else:
        # Adds the product/variant to the cart as a dictionary
        cart[key] = {
            'product_id': product.id,
            'variant_id': variant.id if variant else None,
            'quantity': quantity,
            'price': str(price)
        }

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

        # Ensure that the item exists in the cart
        if str(item_id) in cart:
            if quantity > 0:
                # Update the quantity
                cart[str(item_id)]['quantity'] = quantity
            else:
                # Remove the item if the quantity is 0
                del cart[str(item_id)]

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
        del cart[str(item_id)]

    # Saves the updated cart back to the session
    request.session['cart'] = cart

    # Redirects to the cart detail page
    return redirect('cart_detail')
