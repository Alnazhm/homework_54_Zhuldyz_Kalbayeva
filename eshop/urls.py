from django.urls import path
from eshop.views.products_view import products_view
from eshop.views.product_view import detail_view
from eshop.views.category_add_view import category_add_view
from eshop.views.product_add_view import product_add_view

urlpatterns = [
    path('', products_view, name='products'),
    path('products', products_view, name='products'),
    path('products/<int:pk>', detail_view, name='product'),
    path('categories/add/', category_add_view, name='add_category'),
    path('products/add/', product_add_view, name='add_product')
]