from django.contrib import admin

from users.forms import LoginForm
from .models import Slider

admin.site.site_title = 'Glammer'
admin.site.site_header = 'Glammer Admin Panel'
admin.site.index_title = 'Welcome to Glammer Admin'

admin.site.login_form = LoginForm
admin.site.login_template = 'users/login.html'


class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    ordering = ('order',)

admin.site.register(Slider, SliderAdmin)

