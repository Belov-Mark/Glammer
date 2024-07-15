from django.db import models

class City(models.Model):   
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    reduction = models.CharField(max_length=150, unique=True, blank=True, null=True, verbose_name='Сокращение')

    class Meta:
        db_table = 'city'
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name
