from django.urls import path

from products import views

app_name = 'products'

urlpatterns = [
    path('<int:productId>/', views.product, name='product'),
    path('<slug:categorySlug>/', views.catalog, name='catalog'),
]