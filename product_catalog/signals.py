from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product
from django.utils import timezone
from datetime import timedelta
import logging

logger = logging.getLogger('product_catalog')  

@receiver(post_save, sender=Product)
def update_new_arrivals(sender, instance, created, **kwargs):
    # Prevent re-triggering the signal handler
    if kwargs.get('created', False):
        logger.info(f'New product added: {instance.name}')
    else:
        logger.info(f'Product updated: {instance.name}')

    # Re-evaluate is_new_arrival status for both new and updated products
    new_arrival_status = (
        instance.created_at >= timezone.now() - timedelta(days=30) or
        instance.updated_at >= timezone.now() - timedelta(days=30)
    )

    # Save if the status has changed
    if instance.is_new_arrival != new_arrival_status:
        instance.is_new_arrival = new_arrival_status
        instance.save(update_fields=['is_new_arrival'], force_insert=False)  # Avoid re-triggering signal

