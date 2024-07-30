from django.db import models
from django.conf import settings


class Favorites(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'favorites'
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

class FavoritesItem(models.Model):
    favorites = models.ForeignKey(Favorites, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'favorites_item'
        verbose_name = 'Элемент списка желаний'
        verbose_name_plural = 'Элементы списка желаний'