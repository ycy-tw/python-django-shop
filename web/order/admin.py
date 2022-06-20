from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):

    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = [
        'user', 'email', 'address',
        'paid', 'created', 'updated', 'name'
    ]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline] # include related models on the same edit page.