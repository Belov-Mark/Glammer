from django.contrib import admin

from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1  # Количество дополнительных пустых форм

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__email',)  # Поиск по email пользователя, если он есть
    inlines = [CartItemInline]  # Включаем CartItem как встроенную форму

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    list_filter = ('cart', 'product')
    search_fields = ('product__name',)  # Поиск по названию продукта

# Регистрация моделей
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)

