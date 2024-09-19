from django.db.models.signals import post_save, post_delete
from django.contrib.auth.signals import user_logged_out
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import OrderItem, Order
from cart.models import CartItem
from product_catalog.models import Product, ProductVariant


@receiver(post_save, sender=OrderItem)
def update_order_total_on_save(sender, instance, **kwargs):
    """
    Signal to update the order total when an OrderItem is created or updated.
    """
    order = instance.order
    order.update_total()

@receiver(post_delete, sender=OrderItem)
def update_order_total_on_delete(sender, instance, **kwargs):
    """
    Signal to update the order total when an OrderItem is deleted.
    If the order has no items left, delete the order.
    """
    order = instance.order
    # Recalculate order total after an item is deleted
    order.update_total()

    # If the order has no items left, delete the order
    if order.items.count() == 0:
        order.delete()


# Save cart to database on logout
@receiver(user_logged_out)
def save_cart_on_logout(sender, request, user, **kwargs):
    cart = request.session.get('cart', {})

    if user.is_authenticated and cart:
        for key, item_data in cart.items():
            try:
                product = Product.objects.get(id=item_data['product_id'])
            except Product.DoesNotExist:
                continue  # If product no longer exists, skip this item

            variant = None
            if 'variant_id' in item_data:
                try:
                    variant = ProductVariant.objects.get(id=item_data['variant_id'])
                except ProductVariant.DoesNotExist:
                    pass  # If variant no longer exists, save without it

            # Save each cart item in the database
            CartItem.objects.create(
                user=user,
                product=product,
                variant=variant,
                quantity=item_data['quantity']
            )


# Load cart from database on login
@receiver(user_logged_in)
def load_cart_on_login(sender, request, user, **kwargs):
    # Get all saved cart items for the user
    saved_cart_items = CartItem.objects.filter(user=user)

    # Restore them to the session cart
    cart = request.session.get('cart', {})

    for item in saved_cart_items:
        product_id = str(item.product.id)
        variant_id = item.variant.id if item.variant else None

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            continue  # Skip if the product no longer exists

        cart[product_id] = {
            'product_id': product_id,
            'variant_id': variant_id,
            'quantity': item.quantity,
            'price': str(item.product.price),  # Retrieves the current price
        }

    request.session['cart'] = cart