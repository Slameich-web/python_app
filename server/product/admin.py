from django.contrib import admin

from product.models import Product


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    pass
