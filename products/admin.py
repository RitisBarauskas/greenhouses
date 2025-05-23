from django.contrib import admin

from products.models import Category, Tag, Product, Greenhouse, ProductGreenhouse


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page = 10
    list_display_links = ('id', 'name')
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page = 10
    list_display_links = ('id', 'name')
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'category', 'time_to_grow')
    search_fields = ('name',)
    list_filter = ('category',)
    ordering = ('time_to_grow',)
    list_per_page = 10
    list_display_links = ('id', 'name')
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'category', 'tags', 'time_to_grow')
        }),
    )


@admin.register(Greenhouse)
class GreenhouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'capacity')
    search_fields = ('name',)
    list_filter = ('location',)
    ordering = ('capacity',)
    list_per_page = 10
    list_display_links = ('id', 'name')
    fieldsets = (
        (None, {
            'fields': ('name', 'location', 'capacity')
        }),
    )


@admin.register(ProductGreenhouse)
class ProductGreenhouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'greenhouse')
    search_fields = ('product__name',)
    list_filter = ('greenhouse',)
    ordering = ('product',)
    list_per_page = 10
    list_display_links = ('id', 'product')
    fieldsets = (
        (None, {
            'fields': ('product', 'greenhouse')
        }),
    )