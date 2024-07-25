# Generated by Django 4.2.13 on 2024-07-23 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('citys', '0002_alter_city_reduction'),
        ('users', '0004_user_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='citys.city', verbose_name='Город'),
        ),
    ]