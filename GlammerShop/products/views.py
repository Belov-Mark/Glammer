from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Product

class CatalogView(ListView):
    model = Product
    template_name = 'products/catalog.html'
    context_object_name = 'products'
    paginate_by = 21
    allow_empty = False

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        if category_slug and category_slug != 'all':
            products = super().get_queryset().filter(category__slug=category_slug)
        else:
            products = super().get_queryset()
        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug_url'] = self.kwargs.get('category_slug')
        return context

class ProductView(DetailView):
    model = Product
    template_name = 'products/product.html'
    pk_url_kwarg = 'id'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        product = get_object_or_404(Product, id=self.kwargs.get(self.pk_url_kwarg))
        return product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context

class NewsView(ListView):
    model = Product
    template_name = 'products/news.html'
    context_object_name = 'newProducts'
    paginate_by = 12
    allow_empty = False

    def get_queryset(self):
        return Product.get_recent_products()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newProducts'] = self.get_queryset()
        return context

class SaleView(ListView):
    model = Product
    template_name = 'products/sale.html'
    context_object_name = 'saleProducts'
    paginate_by = 12
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(discount__gt=0)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['saleProducts'] = self.get_queryset()
        return context
