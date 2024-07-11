from django.shortcuts import render

from products.models import Product


def main(request):
    newProducts = Product.objects.all().order_by('-created_at')[:6]
    saleProducts = Product.objects.filter(discount__gt=0).order_by('-created_at')[:3]
    context = {
        'newProducts': newProducts,
        'saleProducts': saleProducts,
    }
    return render(request, 'main/main.html', context)

def contacts(request):
    return render(request, 'main/contacts.html')
