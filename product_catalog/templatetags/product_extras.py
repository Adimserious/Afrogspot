import logging
from django import template

logger = logging.getLogger(__name__)
register = template.Library()

@register.filter
def product_image(product, placeholder='/media/logo.jpg'):
    try:
        # Check if the image exists and the URL is valid
        if product.image and product.image.url:
            return product.image.url
    except ValueError:
        # If there's a missing image or invalid URL, return the placeholder
        return placeholder
    # If no image is provided, return the placeholder
    return placeholder
