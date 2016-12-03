# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20161201_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productpicture',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='on_discount',
        ),
        migrations.AlterField(
            model_name='feature',
            name='name',
            field=models.CharField(max_length=15, verbose_name=b'Nombre'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='discount_percentage',
            field=models.PositiveIntegerField(blank=True, help_text=b'Si esta referencia est\xc3\xa1 en oferta, ingresa el porcentaje de descuento', null=True, verbose_name=b'Porcentaje de descuento'),
        ),
    ]