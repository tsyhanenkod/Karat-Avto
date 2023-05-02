from django.db import models

class Service(models.Model):
    name = models.CharField('Назва сервісу', max_length=100)
    service_image = models.ImageField('Основне зображення', upload_to='services/')
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'services'
        verbose_name = 'Сервіс'
        verbose_name_plural = 'Сервіси'
