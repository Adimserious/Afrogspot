from django.contrib import admin
from .models import Product, Category, Country, ProductVariant, ProductRating


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
        'total_stock_display',
        'stock',
        'is_active',
        'is_new_arrival',
        'created_at',
        'updated_at',
    )

    search_fields = ('name', 'description')
    list_filter = ('is_active', 'is_vegan', 'is_gluten_free', 'is_new_arrival')
    ordering = ('name',)

    # This is the total stock for variants products only
    def total_stock_display(self, obj):
        """Display total stock for products."""
        return obj.total_stock
    total_stock_display.short_description = 'Total Stock'


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('product', 'size', 'price', 'stock')
    list_filter = ('product',)
    search_fields = ('product__name', 'size')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Country)


@admin.register(ProductRating)
class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'created_at')
    search_fields = ('user__username', 'product__name')  # Search functionality
    list_filter = ('rating', 'created_at')  # Filter options in the sidebar
