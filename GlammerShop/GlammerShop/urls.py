from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static

from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('products/', include('products.urls', namespace='products')),
    path('user/', include('users.urls', namespace='users')),
    path('cart/', include('carts.urls', namespace='carts')),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
