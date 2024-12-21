from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from datetime import timedelta


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# custom model
class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=254, null=True, blank=True)
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        related_name='products',
        on_delete=models.SET_NULL
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    stock = models.IntegerField(null=True, blank=True)
    image = models.ImageField(
        null=True,
        blank=True,
        default='static/media/background-image.jpg'
    )
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_vegan = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    expiration_date = models.DateField(null=True, blank=True)
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=1
    )
    is_new_arrival = models.BooleanField(default=False)

    def clean(self):
        if self.price < 0:
            raise ValidationError({'price': 'Price cannot be negative.'})
        if self.discount_price is not None and self.discount_price < 0:
            raise ValidationError({'discount_price': 'Discount price cannot be negative.'})
        if self.discount_price is not None and self.discount_price > self.price:
            raise ValidationError({'discount_price': 'Discount price cannot exceed the base price.'})


    def save(self, *args, **kwargs):
        # Ensures created_at is set when creating a new product
        if not self.pk:
            self.created_at = timezone.now()

        # Mark as new arrival if created or updated within the last 30 days
        recent_threshold = timezone.now() - timedelta(days=30)
        if (self.created_at >= recent_threshold or
                self.updated_at >= recent_threshold):
            self.is_new_arrival = True
        else:
            self.is_new_arrival = False

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def __str__s(self):
        return f"{self.name} - {self.country.name}"

    def is_expired(self):
        if self.expiration_date:
            return self.expiration_date < timezone.now().date()
        return False

    def is_in_stock(self, quantity=1):
        """Check if the product has enough stock
         available for the given quantity."""

        # If stock is not set, consider it as out of stock
        if self.stock is None:
            return False
        return self.stock >= quantity

    @property
    def total_stock(self):
        """Calculate total stock from all variants."""
        return sum(variant.stock for variant in self.variants.all())

    # custom method
    def get_price(self):
        """
        Returns the base price of the product or the price of the first
        variant if variants exist.
        """
        # Check if the product has variants
        if self.variants.exists():
            # displaying the first variant price
            return f"{self.variants.first().price:.2f}"  # Ensure two decimal places
        return f"{self.price:.2f}"  # Default product price

    @classmethod
    def get_new_arrivals(cls):
        """Return products marked as new arrivals."""
        return cls.objects.filter(is_new_arrival=True, is_active=True)


# custom model
class ProductVariant(models.Model):
    product = models.ForeignKey(Product, related_name='variants',
                                on_delete=models.CASCADE)
    size = models.DecimalField(max_digits=5, decimal_places=2)  # Size in kg
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Size Price
    stock = models.IntegerField()  # The stock level for this specific size

    def __str__(self):
        return f"{self.size} kg - {self.product.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Updates the product's total stock after saving the variant
        self.product.save()  # This will update the total stock property


class ProductRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    rating = models.IntegerField()  # Store integer rating (1 to 5 stars)
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rating} stars by {self.user} on {self.product}'
