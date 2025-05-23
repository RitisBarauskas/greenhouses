from django.urls import path

from products.views import ProductListView, ProductDetailView, ProductsCategoryListView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('categories/<int:category_id>/products', ProductsCategoryListView.as_view(), name='products_of_category'),
]