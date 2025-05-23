from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from products.forms import ProductForm
from products.models import Product, Category, Tag


class ProductListView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'


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


class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = 'products/product_create.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('products:product_detail', kwargs={'product_id': self.object.id})


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'products/product_create.html'
    form_class = ProductForm
    pk_url_kwarg = 'product_id'

    def get_success_url(self):
        return reverse('products:product_detail', kwargs={'product_id': self.object.id})
