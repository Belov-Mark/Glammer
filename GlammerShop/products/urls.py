from django.urls import path

from products import views

app_name = 'products'

urlpatterns = [
    path('news/', views.NewsView.as_view(), name='news'),
    path('sale/', views.SaleView.as_view(), name='sale'),
    path('<int:id>/', views.ProductView.as_view(), name='product'),
    path('<slug:category_slug>/', views.CatalogView.as_view(), name='catalog'),
    
]