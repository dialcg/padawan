# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20161201_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='discount_percentage',
            field=models.PositiveIntegerField(blank=True, help_text=b'Si el producto est\xc3\xa1 en oferta, ingresa el porcentaje de descuento de esta referencia', null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='on_discount',
            field=models.BooleanField(default=False, help_text=b'Activa esta opci\xc3\xb3n si esta referencia est\xc3\xa1 en oferta'),
        ),
    ]