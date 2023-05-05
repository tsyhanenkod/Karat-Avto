from django.db import models
from django.urls import reverse
from django.contrib import admin


class Category(models.Model):
    name = models.CharField('Категорія', max_length=100)
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'cars'
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class EngineTypes(models.Model):
    name = models.CharField('Тип двигуна', max_length=100)
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'cars'
        verbose_name = 'Тип двигуна'
        verbose_name_plural = 'Типи двигунів'


class Transmission(models.Model):
    name = models.CharField('Коробка передач', max_length=100)
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'cars'
        verbose_name = 'Коробка передач'
        verbose_name_plural = 'Коробки передач'


class Colors(models.Model):
    name = models.CharField('Колір', max_length=100)
    hex = models.CharField('Hex номер кольору', max_length=100)
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'cars'
        verbose_name = 'Колір'
        verbose_name_plural = 'Кольори'


class CarMark(models.Model):
    name = models.CharField('Марка', max_length=100)
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'cars'
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'


class CarModel(models.Model):
    name = models.CharField('Модель', max_length=100)
    mark = models.ForeignKey(CarMark, verbose_name='', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'cars'
        verbose_name = 'Модель'
        verbose_name_plural = 'Моделі'


# def reverse(param, kwargs):
#     pass

class DriveUnit(models.Model):
    name = models.CharField('Назва приводу', max_length=25)
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'cars'
        verbose_name = 'Привід'
        verbose_name_plural = 'Приводи'


class BodyType(models.Model):
    name = models.CharField('Назва типу кузова', max_length=25)
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'cars'
        verbose_name = 'Тип кузова'
        verbose_name_plural = 'Типи кузовів'


class Car(models.Model):
    mark = models.ForeignKey(CarMark, verbose_name='Марка', on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(CarModel, verbose_name='Модель', on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category, verbose_name='Категорія', blank=True)
    year = models.PositiveSmallIntegerField('Рік випуску', default=2010)

    main_image = models.ImageField('Основне зображення', upload_to='cars/car_main_images/')
    description_uk = models.TextField("Опис автомобіля (мінімум 500 символів)")
    description_en = models.TextField("Опис автомобіля (мінімум 500 символів)")

    price = models.IntegerField('Ціна ($)', default=0)
    price_ua = models.IntegerField('Ціна (грн.)', default=0)

    car_speeds = models.PositiveSmallIntegerField('Кількість передач', default=5)
    engine_type = models.ForeignKey(EngineTypes, verbose_name='Тип двигуна', on_delete=models.SET_NULL, null=True)
    engine_volume = models.PositiveSmallIntegerField("Об'єм двигуна (см^3)", default=0)
    transmission = models.ManyToManyField(Transmission, verbose_name='Коробка передач', blank=True)
    power = models.PositiveSmallIntegerField('Потужність (к.с.)', default=0)
    drive_unit = models.ForeignKey(DriveUnit, verbose_name='Привід', on_delete=models.SET_NULL, null=True)

    body_type = models.ForeignKey(BodyType, verbose_name="Тип кузова", on_delete=models.SET_NULL, null=True)
    car_weight = models.FloatField('Масс авто', default=0)
    dimensions = models.CharField('Габарити (позначати як ДхШхВ)')
    color = models.ManyToManyField(Colors, verbose_name='Колір', blank=True)

    draft = models.BooleanField('Чернетка', default=False)
    url = models.SlugField(max_length=100)

    def __str__(self):
        return f"{self.mark} {self.model}"

    class Meta:
        app_label = 'cars'
        verbose_name = 'Автомобіль'
        verbose_name_plural = 'Автомобілі'


class CarImages(models.Model):
    name = models.CharField('Назва зображення', max_length=25)
    car = models.ForeignKey(Car, verbose_name='Автомобіль', on_delete=models.CASCADE)
    image = models.ImageField('Зображення', upload_to='cars/car_images_lists/')

    def __str__(self):
        return f"{self.name} - {self.car}"

    class Meta:
        app_label = 'cars'
        verbose_name = 'Зображення'
        verbose_name_plural = 'Зображення'