from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderItem, Order

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
    """
    order = instance.order
    order.update_total()
