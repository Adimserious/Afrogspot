from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Number of empty forms to display initially
    fields = ('product', 'variant', 'quantity', 'price', 'total_price')
    readonly_fields = ('total_price',)  # read-only
    can_delete = True
    show_change_link = True


class OrderAdmin(admin.ModelAdmin):
    # Displays these fields in the admin list view
    list_display = ('order_number', 'user', 'order_total', 'order_status', 'date_ordered')
    
    # Adds filters in the admin interface
    list_filter = ('order_status', 'date_ordered')
    
    # Searchs by these fields
    search_fields = ('order_number', 'user__username', 'user__email')
    # Read only
    readonly_fields = ('order_number', 'date_ordered', 'delivery_cost', 'order_total', 'grand_total',)
    inlines = [OrderItemInline]
    ordering = ('-date_ordered',)

    def get_readonly_fields(self, request, obj=None):
        """
        Returns the list of fields that should be read-only. The fields is conditional based on
        whether the object is being created or edited.
        """
        if obj:  # Editing an existing order
            return self.readonly_fields + ('order_number', 'date_ordered', 'grand_total')
        return self.readonly_fields

admin.site.register(Order, OrderAdmin)