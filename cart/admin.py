from django.contrib import admin
from .models import CartItem

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'variant', 'quantity')
    search_fields = ('user__username', 'product__name')
    list_filter = ('user', 'product', 'variant')

