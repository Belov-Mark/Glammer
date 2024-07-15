from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('name', 'surname', 'number', 'email', 'is_active', 'is_staff')
    search_fields = ('name', 'surname', 'number', 'email')
    list_filter = ('name', 'surname', 'email', 'is_staff')
    fieldsets = (
        ('Основная информация', {'fields': ('email', 'password')}),
        ('Персональная информация', {'fields': ('name', 'surname', 'number', 'date', 'sex')}),
        ('Разрешения', {'fields': ('is_staff',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)