from django.db import models
from django.conf import settings
from product_catalog.models import Product, ProductVariant
from decimal import Decimal
import uuid
from django.db.models import Sum


# Function to generate a short order number
def generate_short_order_number():
    # Return the first 8 characters of a UUID
    return str(uuid.uuid4())[:8]

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=50)
    date_ordered = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, default=7.00)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stripe_payment_intent = models.CharField(max_length=200, null=True, blank=True)
    order_number = models.CharField(max_length=8, default=generate_short_order_number, null=False, editable=False, unique=True)
    payment_status = models.CharField(max_length=10, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded')], default='pending')
    order_status = models.CharField(max_length=12, choices=[
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled')], default='processing')
    

    def update_total(self):
        """
        Updates grand total by adding delivery cost to the order total.
        """
        self.grand_total = self.order_total + Decimal(self.delivery_cost)
        if self.grand_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.grand_total * settings.STANDARD_DELIVERY
        else:
            self.delivery_cost = 0
        self.order_total = self.grand_total + self.delivery_cost
        self.save()

    def __str__(self):
        return f'Order #{self.order_number} by {self.full_name}'

