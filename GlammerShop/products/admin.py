from django.contrib import admin

from products.models import Categories, Product, Subcategory


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount', 'quantity', 'id')
    list_editable = ('price', 'discount', 'quantity')
    search_fields =  ('name', 'price', 'discount', 'id')
    list_filter = ('name', 'price', 'discount', 'quantity', 'category', 'subcategory')
    fields = (('name', 'id'),
              ('price', 'discount'),
              'quantity',
              'image',
              ('category', 'subcategory'),
              'description')