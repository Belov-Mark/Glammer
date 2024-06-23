# Generated by Django 4.2.13 on 2024-06-13 13:59

from django.db import migrations, models
import products.utils


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.CharField(default=products.utils.generate_unique_id, max_length=6, primary_key=True, serialize=False, unique=True),
        ),
    ]
