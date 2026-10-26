from django.contrib import admin
from FarmersMarket.products.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'unit',)
    list_filter = ('category',)
    search_fields = ('name',)
