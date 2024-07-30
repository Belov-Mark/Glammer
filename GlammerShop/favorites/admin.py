from django.contrib import admin

from .models import Favorites,  FavoritesItem


class FavoritesItemInline(admin.TabularInline):
    model = FavoritesItem
    extra = 1


class FavoritesAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__email',)
    inlines = [FavoritesItemInline]

class FavoritesItemAdmin(admin.ModelAdmin):
    list_display = ('favorites', 'product')
    list_filter = ('favorites', 'product')
    search_fields = ('product__name',)

admin.site.register(Favorites, FavoritesAdmin)
admin.site.register(FavoritesItem, FavoritesItemAdmin)
