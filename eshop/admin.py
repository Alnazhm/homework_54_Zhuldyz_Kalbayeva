from django.contrib import admin
from eshop.models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_filter = ('id', 'title', 'description')
    search_fields = ('title', 'description')
    fields = ('title', 'description')

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'product_description', 'price', 'images_url', 'created_at', 'changed_at')
    list_filter = ('id', 'title', 'product_description', 'price', 'images_url', 'created_at', 'changed_at')
    search_fields = ('title', 'product_description', 'price', 'images_url')
    fields = ('title', 'product_description', 'price', 'images_url')

admin.site.register(Product, ProductAdmin)