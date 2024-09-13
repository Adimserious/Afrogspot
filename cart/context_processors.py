from decimal import Decimal
from django.conf import settings
from product_catalog.models import Product, ProductVariant
from django.shortcuts import get_object_or_404


def cart_content(request):
    cart_items = []
    total = Decimal(0)
    product_count = 0
    cart = request.session.get('cart', {})

    # Free delivery threshold and standard delivery fee
    FREE_DELIVERY_THRESHOLD = Decimal(50.00)  # Free delivery for totals above 50 euros
    STANDARD_DELIVERY_FEE = Decimal(7.00)     # Fixed delivery fee of 7 euros

    for key, item_data in cart.items():
        # Ensures item_data is a dictionary
        if isinstance(item_data, dict):
            product = get_object_or_404(Product, pk=item_data['product_id'])
            variant = None

            if item_data.get('variant_id'):
                variant = get_object_or_404(ProductVariant, pk=item_data['variant_id'])
                price = Decimal(variant.price)
            else:
                price = Decimal(product.price)

            total += price * item_data['quantity']
            product_count += item_data['quantity']

            cart_items.append({
                'product': product,
                'variant': variant,
                'quantity': item_data['quantity'],
                'price': price,
                'total_price': price * item_data['quantity']
            })

    # Apply delivery charges based on the total and only if cart is not empty
    if total > 0:
        if total < FREE_DELIVERY_THRESHOLD:
            delivery = STANDARD_DELIVERY_FEE  # Set delivery fee to €7
            free_delivery_delta = FREE_DELIVERY_THRESHOLD - total
        else:
            delivery = Decimal(0)  # Free delivery
            free_delivery_delta = Decimal(0)
        grand_total = delivery + total
    else:
        delivery = Decimal(0)  # No delivery charge for an empty cart
        free_delivery_delta = Decimal(0)
        grand_total = Decimal(0)

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
