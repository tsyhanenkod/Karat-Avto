from django.db import models

class BannerList(models.Model):
    name = models.CharField('Назва баннера', max_length=25)
    image = models.ImageField('Зображення', upload_to='banners/')

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'base'
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннери'
