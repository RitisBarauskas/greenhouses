from django.contrib.auth import get_user_model
from django.db import models

from products.constants import CHAR_FIELD_MAX_LENGTH


User = get_user_model()


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=CHAR_FIELD_MAX_LENGTH)
    description = models.TextField(verbose_name='Описание категории')

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(verbose_name='Название тега', max_length=CHAR_FIELD_MAX_LENGTH)
    description = models.TextField(verbose_name='Описание тега')

    class Meta:
        verbose_name_plural = 'Тег'
        verbose_name = 'Теги'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name='Название продукта', max_length=CHAR_FIELD_MAX_LENGTH)
    description = models.TextField(verbose_name='Описание продукта')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, related_name='products')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    time_to_grow = models.IntegerField(verbose_name='Время роста (в днях)')
    creator = models.ForeignKey(
        User,
        verbose_name='Ответственное лицо',
        on_delete=models.SET_NULL,
        related_name='products',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукт'

    def __str__(self):
        return self.name


class Greenhouse(models.Model):
    name = models.CharField(verbose_name='Название теплицы', max_length=CHAR_FIELD_MAX_LENGTH)
    location = models.CharField(verbose_name='Местоположение', max_length=CHAR_FIELD_MAX_LENGTH)
    capacity = models.IntegerField(verbose_name='Вместимость')

    class Meta:
        verbose_name_plural = 'Теплицы'
        verbose_name = 'Теплица'

    def __str__(self):
        return self.name


class ProductGreenhouse(models.Model):
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    greenhouse = models.ForeignKey(Greenhouse, verbose_name='Теплица', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    manager = models.ForeignKey(
        User,
        verbose_name='Менеджер',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='greenhouses',
    )

    class Meta:
        verbose_name_plural = 'Продукты в теплицах'
        verbose_name = 'Продукт в теплице'

    def __str__(self):
        return f'{self.product.name} in {self.greenhouse.name}'
