# Generated by Django 4.2 on 2023-05-04 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complect', '0003_alter_char_name_alter_char_name_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prices',
            name='price_bf',
            field=models.CharField(max_length=100, null=True, verbose_name='Ціна комплектації + чорний дах'),
        ),
    ]
