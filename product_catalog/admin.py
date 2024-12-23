from django.contrib import admin
from .models import Product, Category, Country, ProductVariant, ProductRating, ProductImage


# Admin class for the Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


# Inline model for additional product images
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3  # Number of additional image fields displayed initially
    fields = ('image', 'alt_text')
    verbose_name = "Additional Image"
    verbose_name_plural = "Additional Images"


# Admin class for the Product model
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
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
    inlines = [ProductImageInline]  # Include the inline form for additional images

    # This is the total stock for variant products only
    def total_stock_display(self, obj):
        """Display total stock for products."""
        return obj.total_stock
    total_stock_display.short_description = 'Total Stock'


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('product', 'size', 'price', 'stock')
    list_filter = ('product',)
    search_fields = ('product__name', 'size')


@admin.register(ProductRating)
class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'created_at')
    search_fields = ('user__username', 'product__name')  # Search functionality
    list_filter = ('rating', 'created_at')  # Filter options in the sidebar


# Register the remaining models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Country)
