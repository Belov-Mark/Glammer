from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='Email')
    name = models.CharField(max_length=30, verbose_name='Имя')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    number = models.CharField(max_length=15, verbose_name='Контактный телефон')
    sex = models.CharField(max_length=1, choices=[('M', 'М'), ('F', 'Ж')], verbose_name='Пол')
    date = models.DateField(verbose_name='Дата рождения')
    city = models.ForeignKey('citys.City', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Город')

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        verbose_name='Группы',
        related_name='user_set',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        verbose_name='Разрешения',
        related_name='user_set',
        related_query_name='user',
    )

    date_joined = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname', 'number', 'sex', 'date']

    def __str__(self):
        return f'{self.name} {self.surname}'
    
    def get_short_name(self):
        '''
        Получение имени пользователя
        '''
        return self.name
    
    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Отправка электронного письма пользователю
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
