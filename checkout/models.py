from django.db import models
from django.conf import settings
from product_catalog.models import Product, ProductVariant
from decimal import Decimal
import uuid
from django.db.models import Sum
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.models import Profile


# Function to generate a short order number
def generate_short_order_number():
    # Return the first 8 characters of a UUID
    return str(uuid.uuid4())[:8]


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )
    profile = models.ForeignKey(
        'profiles.Profile',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=50, blank=False, null=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, default=7.00)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stripe_payment_intent = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )  # Stores Stripe payment intent ID
    order_number = models.CharField(
        max_length=8,
        default=generate_short_order_number,
        null=False,
        editable=False,
        unique=True
    )
    payment_status = models.CharField(
        max_length=10,
        choices=[
            ('pending', 'Pending'),
            ('completed', 'Completed'),
            ('failed', 'Failed'),
            ('refunded', 'Refunded')
        ],
        default='pending'
    )
    order_status = models.CharField(
        max_length=12,
        choices=[
            ('processing', 'Processing'),
            ('shipped', 'Shipped'),
            ('delivered', 'Delivered'),
            ('cancelled', 'Cancelled')
        ],
        default='processing'
    )

    def update_total(self):
        """
        Updates grand total by recalculating order total and delivery cost.
        Clears the delivery cost if the order total is zero.
        """
        # Calculate the new order total by summing all order item totals
        self.order_total = sum(item.total_price for item in self.items.all())

        # If the order total is zero, clear the delivery cost
        if self.order_total == 0:
            # Clear delivery cost if no items in the order
            self.delivery_cost = Decimal(0.00)
        elif self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = Decimal(7.00)  # Standard delivery cost
        else:
            self.delivery_cost = Decimal(0.00)  # Free delivery for orders above the threshold

        # Calculate the grand total
        self.grand_total = self.order_total + self.delivery_cost

        # Save the order to update the totals
        self.save()

    def __str__(self):
        return f'Order #{self.order_number} by {self.full_name}'


# stores information about each product that the customer has purchased
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False
    )

    def save(self, *args, **kwargs):
        """
        Calculates the total price for the order item (price * quantity).
        If quantity is zero, automatically delete the order item.
        """
        if self.quantity == 0:
            self.delete()
        else:
            self.total_price = self.price * self.quantity
            super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.quantity} x {self.product.name} (Order #{self.order.id})'

    def delete(self, *args, **kwargs):
        """
        If an OrderItem is deleted, restock the product.
        """
        self.product.stock += self.quantity
        self.product.save()
        super().delete(*args, **kwargs)
