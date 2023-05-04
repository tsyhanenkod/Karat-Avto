from django.db import models
from cars.models import *


class Charcategory(models.Model):
    name = models.CharField('Назва категорії характеристик', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'complect'
        verbose_name = 'Категорія характеристики'
        verbose_name_plural = 'Категорії характеристик'


class Char(models.Model):
    name = models.CharField('Назва характеристики', max_length=100, unique=True)
    char_category = models.ForeignKey(Charcategory, verbose_name='Категорія характеристик', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'complect'
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'


class Complect(models.Model):
    name = models.CharField('Назва комплектації', max_length=50)
    car = models.ForeignKey(Car, verbose_name='Автомобіль', on_delete=models.SET_NULL, null=True)
    char_category = models.ManyToManyField(Charcategory, verbose_name='Категорія характеристик', null=False)
    drive_unit = models.ForeignKey(DriveUnit, verbose_name='Привід', on_delete=models.SET_NULL, null=True)
    char = models.ManyToManyField(Char, verbose_name='Список характеристик в комплектації', null=True)


    def __str__(self):
        return self.name

    class Meta:
        app_label = 'complect'
        verbose_name = 'Комплектація'
        verbose_name_plural = 'Комплектації'


class Values(models.Model):
    complectation = models.ForeignKey(Complect, verbose_name='Комплектація', on_delete=models.CASCADE)
    char = models.ForeignKey(Char, verbose_name='Характеристика', on_delete=models.SET_NULL, null=True)
    value = models.BooleanField('Наявність в комплектації', default=False)

    class Meta:
        app_label = 'complect'
        verbose_name = 'Значення'
        verbose_name_plural = 'Значення'


class Prices(models.Model):
    complectation = models.ForeignKey(Complect, verbose_name='Комплектація', on_delete=models.CASCADE)
    transmission = models.ForeignKey(Transmission, verbose_name='Коробки передач', on_delete=models.SET_NULL, null=True)
    price = models.CharField('Ціна комплектації', max_length=100)
    price_bf = models.CharField('Ціна комплектації + чорний дах (0 якщо не потрібно)', max_length=100, null=True, default=0)