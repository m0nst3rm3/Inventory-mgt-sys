from django.contrib import admin

from .models import (
    Supplier,
    Buyer,
    Product,
    Order,
)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']


class BuyerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Product)
admin.site.register(Order)