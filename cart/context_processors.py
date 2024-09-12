from decimal import Decimal
from django.conf import settings
from product_catalog.models import Product
from django.shortcuts import get_object_or_404

# code and inspiration here are from the boutique ado Walkthrough
def cart_content(request):
    cart_items = []
    total = Decimal(0)
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        # Ensure item_data is a dictionary and quantity is extracted correctly
        if isinstance(item_data, dict):
            quantity = item_data.get('quantity', 0)
        else:
            # If item_data is not a dict, it's probably just the quantity (legacy data)
            quantity = item_data

        # Ensure quantity is always treated as an integer
        try:
            quantity = int(quantity)
        except (ValueError, TypeError):
            quantity = 0

        
        product = get_object_or_404(Product, pk=item_id)
        total += Decimal(quantity) * product.price
        product_count += (quantity) 
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })
    
    if request.user.is_authenticated:
        if total < settings.FREE_DELIVERY_THRESHOLD:
            delivery = total * Decimal(settings.STANDARD_DELIVERY)
            free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
        else:
            delivery = Decimal(0)
            free_delivery_delta = Decimal(0)
        grand_total = delivery + total
    
    else:
        delivery = Decimal(0)
        free_delivery_delta = Decimal(0)
        grand_total = total

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
