from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Number of empty forms to display initially
    fields = ('product', 'variant', 'quantity', 'price', 'total_price')
    readonly_fields = ('total_price',)  # Read-only
    can_delete = True
    show_change_link = True


class OrderAdmin(admin.ModelAdmin):
    """Admin configuration for the Order model."""

    # Display fields in the admin list view
    list_display = (
        'order_number',
        'user',
        'profile',
        'payment_method', 
        'paypal_payment_id',  
        'order_total',
        'delivery_cost',
        'grand_total',
        'order_status',
        'date_ordered'
    )

    # Adds filters in the admin interface
    list_filter = ('order_status', 'date_ordered', 'payment_method')  # New filter

    # Search by these fields
    search_fields = (
        'order_number',
        'user__username',
        'user__email',
        'paypal_payment_id',
    )

    # Read-only fields
    readonly_fields = (
        'order_number',
        'payment_method',  # New read-only field
        'paypal_payment_id',  # New read-only field
        'date_ordered',
        'delivery_cost',
        'order_total',
        'grand_total'
    )

    inlines = [OrderItemInline]
    ordering = ('-date_ordered',)

    def get_readonly_fields(self, request, obj=None):
        """Returns list of read-only fields."""
        return self.readonly_fields


admin.site.register(Order, OrderAdmin)
