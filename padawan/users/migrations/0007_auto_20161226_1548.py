# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-26 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20161221_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_number',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]