from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from products.models import Category, Tag, Product, Greenhouse, ProductGreenhouse
from api.serializers import (
    GreenhouseSerializer,
    CategorySerializer,
    TagSerializer,
    ProductOutSerializer,
    ProductInSerializer,
    ProductGreenhouseOutSerializer,
    ProductGreenhouseInSerializer,
)


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class GreenhouseViewSet(ModelViewSet):
    queryset = Greenhouse.objects.all()
    serializer_class = GreenhouseSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('category', 'creator').prefetch_related('tags')

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProductOutSerializer
        return ProductInSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class ProductGreenhouseViewSet(ModelViewSet):
    queryset = ProductGreenhouse.objects.select_related(
        'product__category',
        'greenhouse',
        'manager',
    ).prefetch_related('product__tags')

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProductGreenhouseOutSerializer
        return ProductGreenhouseInSerializer
