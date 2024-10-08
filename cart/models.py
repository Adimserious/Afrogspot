from django.db import models
from django.contrib.auth.models import User
from product_catalog.models import Product, ProductVariant


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, null=True, 
                                blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.product.name} (Cart of {self.user.username})'