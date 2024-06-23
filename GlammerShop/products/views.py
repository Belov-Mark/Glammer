from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator


from .models import Product



def catalog(request, categorySlug):
    if categorySlug == "all":
        products = Product.objects.all()
    else:
        products = get_object_or_404(Product.objects.filter(category__slug=categorySlug))
    #
    paginator = Paginator(products, 3)
    currentPage = paginator.page()
    #
    context = {
        "products": currentPage,
    }
    return render(request, 'products/catalog.html', context)



def product(request, productId):
    product = Product.objects.get(id=productId) 
    context = {
        "product": product,
    }
    return render(request, 'products/product.html', context)

