from django.contrib import admin

from order.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created', 'update', 'payment',)
    list_filter = ('payment',)
    inlines = (OrderItemInline,)
