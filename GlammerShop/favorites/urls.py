from django.urls import path

from . import views


app_name = 'favorite'

urlpatterns = [
    path('favorite/', views.FavorietsView.as_view(), name='favorite'),
    path('favorite/add/', views.AddToFavoritesView.as_view(), name='add_to_favorite'),
]