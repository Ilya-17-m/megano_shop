from django.contrib import admin

from .models import OrderModel


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = 'pk','address', 'city'
    list_display_links = 'pk',
    search_fields = 'address', 'city'
    fieldsets = [
        (None, {
            'fields': ('city', 'address', 'status',
                       'deliveryType', 'paymentType', 'totalCost', 'createdAt', 'user', 'products', 'profile')
        }),
    ]
