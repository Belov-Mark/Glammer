from django.urls import path

from carts import views

app_name = 'cart'

urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('cart-add/', views.CartAddView.as_view(), name='cart_add'),
    path('cart-change/', views.CartChangeView.as_view(), name='cart_change'),
    path('cart-remove/', views.CartRemoveView.as_view(), name='cart_remove'),
]