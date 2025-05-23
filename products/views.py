from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from products.models import Product, Category, Tag


class ProductListView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
    queryset = Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'


class ProductsCategoryListView(ListView):
    template_name = 'products/products_of_category.html'
    context_object_name = 'products'
    category = None

    def _load_category(self):
        if self.category is None:
            category_id = self.kwargs.get('category_id')
            self.category = get_object_or_404(Category, id=category_id)

    def get_queryset(self):
        self._load_category()
        return self.category.products.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self._load_category()
        context['category'] = self.category
        return context
