from django.db import models

class Category(models.Model):
    title = models.CharField(verbose_name="Категория", max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name="Описание", max_length=500, null=True, blank=True)


    def __str__(self):
        return f"{self.title} - {self.description}"

class Product(models.Model):
    category = models.ForeignKey(verbose_name='Категория', to='eshop.Category', null=False, blank=False, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Категория', max_length=200, null=False, blank=False)
    product_description = models.TextField(verbose_name="Описание", max_length=500, null=True, blank=True)
    price = models.DecimalField(verbose_name="Стоимость", max_digits=22, decimal_places=0)
    images_url = models.TextField(verbose_name="Ссылка на изображение", max_length=3000, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

