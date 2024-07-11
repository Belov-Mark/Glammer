from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.db.models import Count

from .models import Product, Categories


def catalog(request, categorySlug):
    if categorySlug == "all" or not categorySlug:
        products = Product.objects.all()
    else:
        category = get_object_or_404(Categories, slug=categorySlug)
        products = Product.objects.filter(category=category)
    
    # Пагинация
    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    currentPage = paginator.get_page(page_number)
    
    # Получить количество товаров для каждой категории
    categoriesWithProductCount = Categories.objects.annotate(productCount=Count('product'))

    context = {
        "products": currentPage,
        "categoriesWithProductCount": categoriesWithProductCount,
    }
    return render(request, 'products/catalog.html', context)


def product(request, productId):
    product = get_object_or_404(Product, id=id)
    context = {
        "product": product,
    }
    return render(request, 'products/product.html', context)

def news(request):
    newProducts = Product.objects.all().order_by('-created_at')[:6]
    context = {
        "newProducts": newProducts,
    }
    return render(request, 'products/news.html', context)

def sale(request):
    saleProducts = Product.objects.filter(discount__gt=0)
    context = {
        "saleProducts": saleProducts,
    }
    return render(request, 'products/sale.html', context)