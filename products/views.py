from django.http import HttpResponse
from django.shortcuts import render

from products.constants import DATABASE


def index(request):
    products = DATABASE.get('products', [])
    context = {
        'products': products,
    }
    return render(request, 'index.html', context)


def product_detail(request, product_id):
    products = DATABASE.get('products', [])
    product = None
    for item in products:
        if item['id'] == product_id:
            product = item
            break

    if product is None:
        return HttpResponse('Product not found', status=404)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def products_of_category(request, category_id):
    categories = DATABASE.get('categories', [])
    category = None
    for item in categories:
        if item['id'] == category_id:
            category = item
            break

    if category is None:
        return HttpResponse('Category not found', status=404)

    products = DATABASE.get('products', [])
    filtered_products = [product for product in products if product['category_id'] == category_id]

    context = {
        'category': category,
        'products': filtered_products,
    }

    return render(request, 'products/products_of_category.html', context)
