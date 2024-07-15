from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import date

class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30, verbose_name='Имя')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    number = models.CharField(max_length=15, verbose_name='Контактный телефон')
    date = models.DateField(verbose_name='Дата рождения')
    sex = models.CharField(max_length=1, verbose_name='Пол', choices=(('M', 'Мужской'), ('F', 'Женский')))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'surname', 'number',  'date', 'sex']

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.name} {self.surname}'
