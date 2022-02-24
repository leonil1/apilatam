from django.contrib import admin

from apps.store.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_status', 'image', 'stock', 'price', 'category', 'brand')
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)