from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from products.models import Product
from .models import FavoritesItem
from .forms import AddToFavoritesForm
from .mixins import ReceivingFavoritesMixin


class FavorietsView(ReceivingFavoritesMixin, View):
    def get(self, request):
        favorites = self.get_favorites(request)

        response = render(request, 'favorites/favorites.html', {'favorites': favorites})

        # Устанавливаем куки, если это новый favorites_cookie
        if not request.user.is_authenticated:
            favorites_cookie = request.COOKIES.get('favorites_cookie')
            if favorites_cookie:
                response.set_cookie('favorites_cookie', favorites_cookie)

        return response
    
    def post(self, request):
        action = request.POST.get('action')
        favorites = self.get_favorites(request)

        if action == 'add':
            form = AddToFavoritesForm(request.POST)
            if form.is_valid():
                product_id = form.cleaned_data['product_id']
                product = get_object_or_404(Product, id=product_id)
                favorite_item, created = FavoritesItem.objects.get_or_create(favorites=favorites, product=product)
                favorite_item.save()
        
        elif action == 'remove':
            product_id = request.POST.get('product_id')
            favorite_item = get_object_or_404(FavoritesItem, favorites=favorites, product_id=product_id)
            favorite_item.delete()
        
        elif action == 'clear':
            favorites.items.all().delete()

        return redirect(request.META.get('HTTP_REFERER', '/'))
    
class AddToFavoritesView(ReceivingFavoritesMixin, View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        favorites = self.get_favorites(request)
        favorite_item, created = FavoritesItem.objects.get_or_create(favorites=favorites, product=product)
        favorite_item.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
