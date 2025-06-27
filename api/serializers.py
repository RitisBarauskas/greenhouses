from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from products.models import Category, Tag, Product, Greenhouse, ProductGreenhouse

User = get_user_model()


class UserSerializer(ModelSerializer):
    products_count = IntegerField(source='products.count', read_only=True)
    greenhouses_count = IntegerField(source='greenhouses.count', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'products_count', 'greenhouses_count']
        read_only_fields = ['id']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class GreenhouseSerializer(ModelSerializer):
    class Meta:
        model = Greenhouse
        fields = '__all__'


class ProductOutSerializer(ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductInSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'tags', 'time_to_grow', 'creator']
        read_only_fields = ['creator']

    def to_representation(self, instance):
        return ProductOutSerializer(instance).data

    def validate_name(self, value):
        if value.lower() in [None, 'запрещенка']:
            raise ValidationError("Вы не можете использовать это название.")
        return value


class ProductGreenhouseOutSerializer(ModelSerializer):
    greenhouse = GreenhouseSerializer()
    product = ProductOutSerializer()
    manager = UserSerializer(read_only=True)

    class Meta:
        model = ProductGreenhouse
        fields = '__all__'


class ProductGreenhouseInSerializer(ModelSerializer):
    class Meta:
        model = ProductGreenhouse
        fields = ['product', 'greenhouse', 'manager']

    def to_representation(self, instance):
        return ProductGreenhouseOutSerializer(instance).data
