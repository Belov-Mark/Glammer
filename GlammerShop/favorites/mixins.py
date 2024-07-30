from .models import Favorites


class ReceivingFavoritesMixin:
    def get_favorites(self, request):
        if request.user.is_authenticated:
            favorites, created = Favorites.objects.get_or_create(user=request.user)
        else:
            favorites_cookie = request.COOKIES.get('favorites_cookie')
            if not favorites_cookie:
                favorites = Favorites.objects.create()
                request.session['favorites_id'] = favorites.id
            else:
                favorites = Favorites.objects.get(id=favorites_cookie)
        return favorites