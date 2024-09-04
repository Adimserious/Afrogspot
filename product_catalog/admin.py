from django.contrib import admin
from .models import Product, Category

# Classes from the Boutique Ado Walkthrough project of the code institute.

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'stock',
        'image',
    )

    ordering = ('-sku',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
