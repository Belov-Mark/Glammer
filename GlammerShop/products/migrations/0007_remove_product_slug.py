# Generated by Django 4.2.13 on 2024-06-17 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_product_old_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
