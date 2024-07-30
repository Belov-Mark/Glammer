from django.conf import settings
from django.db import models

from products.models import Product

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Пользователь')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    class Meta:
        db_table = 'cart'
        verbose_name = 'Корзину'
        verbose_name_plural = 'Корзины'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE, verbose_name='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='')
    quantity = models.PositiveIntegerField(default=1, verbose_name='')

    class Meta:
        db_table = 'cart_item'
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'

