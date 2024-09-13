from decimal import Decimal
from django.conf import settings
from product_catalog.models import Product, ProductVariant
from django.shortcuts import get_object_or_404


def cart_content(request):
    cart_items = []
    total = Decimal(0)
    product_count = 0
    cart = request.session.get('cart', {})

    for key, item_data in cart.items():
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

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total

    else:
        delivery = 0
        free_delivery_delta = 0
        grand_total = delivery + total

        cart_items.append({
            'product': product,
            'variant': variant,
            'quantity': item_data['quantity'],
            'price': price,
            'total_price': price * item_data['quantity']
        })
    
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
    
    return context