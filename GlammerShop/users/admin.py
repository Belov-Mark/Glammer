from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import SignInForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    model = User
    form = UserChangeForm
    add_form = SignInForm
    list_display = ('name', 'surname', 'number', 'email', 'city', 'is_superuser')
    search_fields = ('name', 'surname', 'number', 'email')
    list_filter = ('name', 'surname', 'email', 'city', 'is_staff', 'is_superuser')
    fieldsets = (
        ('Основная информация', {'fields': ('email', 'password')}),
        ('Персональная информация', {'fields': ('name', 'surname', 'number', 'date', 'sex', 'city')}),
        ('Разрешения', {'fields': ('is_staff', 'groups', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'surname', 'sex', 'date', 'number', 'city', 'is_staff', 'is_active', 'is_superuser'),}
        ),
    )
    ordering = ('email',)

admin.site.register(User, UserAdmin)