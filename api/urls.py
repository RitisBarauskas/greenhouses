from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import CategoryViewSet, TagViewSet, GreenhouseViewSet, ProductViewSet, ProductGreenhouseViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'greenhouses', GreenhouseViewSet, basename='greenhouse')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'product-greenhouses', ProductGreenhouseViewSet, basename='productgreenhouse')

urlpatterns = [
    path('', include(router.urls)),
]