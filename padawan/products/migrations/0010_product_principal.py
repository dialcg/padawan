# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 14:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0015_fill_filter_spec_field'),
        ('products', '0009_auto_20161202_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='principal',
            field=models.ForeignKey(blank=True, help_text=b'Imagen principal de tu producto', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
