from django.urls import path

from products import views

app_name = 'products'

urlpatterns = [
    path('news/', views.news, name='news'),
    path('sale/', views.sale, name='sale'),
    path('<int:productId>/', views.product, name='product'),
    path('<slug:categorySlug>/', views.catalog, name='catalog'),
    
]