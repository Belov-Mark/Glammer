from tabnanny import verbose
from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Заголовок')
    image = models.ImageField(upload_to='slider_images/', verbose_name='Изображение')
    order = models.PositiveIntegerField(default=0, help_text="Порядок слайда", verbose_name='Порядок')

    def save(self, *args, **kwargs):
        # Определяем заголовок на основе значения поля order
        if self.order <= 10:
            self.title = "Первый банер"
        else:
            self.title = "Второй банер"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'

