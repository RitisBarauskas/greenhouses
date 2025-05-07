from django.urls import path

from products.views import index, product_detail, products_of_category

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('categories/<int:category_id>/products', products_of_category, name='products_of_category'),
]