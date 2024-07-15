from django.contrib import admin

from .models import City


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'reduction')
    list_editable = ('reduction',)
    search_fields =  ('name', 'reduction')

admin.site.register(City, CityAdmin)
