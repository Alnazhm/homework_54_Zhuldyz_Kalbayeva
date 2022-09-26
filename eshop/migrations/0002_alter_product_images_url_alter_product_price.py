# Generated by Django 4.1.1 on 2022-09-26 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images_url',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Ссылка на изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=22, verbose_name='Стоимость'),
        ),
    ]