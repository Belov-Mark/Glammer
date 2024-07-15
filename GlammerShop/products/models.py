from datetime import timedelta
from django.utils import timezone
from django.db import models

from .utils import generate_unique_id


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = 'subcategory'
        verbose_name = 'Подкатегорию'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name



class Product(models.Model):
    id = models.CharField(max_length=6, primary_key=True, default=generate_unique_id, unique=True)
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    price = models.DecimalField(default=0, max_digits=7, decimal_places=0, verbose_name='Цена')
    discount = models.DecimalField(default=0, max_digits=3, decimal_places=0, null=True, blank=True, verbose_name='Скидка в %')
    quantity = models.PositiveBigIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')
    subcategory = models.ForeignKey(to=Subcategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ("id",)
    
    def __str__(self):
        return f'{self.name} ({self.id})'

    def sellPrice(self):
        if self.discount:
            number = self.price - self.price * self.discount / 100
            if (number - int(number)) == 0.5:
                return int(number) + 1 if number > 0 else int(number) - 1
            else:
                return round(number)

        return self.price
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = generate_unique_id()
            while Product.objects.filter(id=self.id).exists():
                self.id = generate_unique_id()
        super(Product, self).save(*args, **kwargs)
    
    @staticmethod
    def get_recent_products(days=30):
        recent_date = timezone.now() - timedelta(days=days)
        return Product.objects.filter(created_at__gte=recent_date)
    
    
    

