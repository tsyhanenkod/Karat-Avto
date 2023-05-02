from django.db import models


class Product(models.Model):
    name_uk = models.CharField('uk Назва продукту/послуги', max_length=100)
    name_en = models.CharField('en Назва продукту/послуги', max_length=100)
    description_uk = models.TextField('Опис продукту uk (бажано 500 символів)')
    description_en = models.TextField('Опис продукту en (бажано 500 символів)')
    product_image = models.ImageField('Основне зображення', upload_to='equipment/')

    draft = models.BooleanField('Чернетка', default=False)
    url = models.SlugField(max_length=20)
