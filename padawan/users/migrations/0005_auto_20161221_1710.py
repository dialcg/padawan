# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-21 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20161221_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_type',
            field=models.CharField(blank=True, choices=[(b'CC', b'C\xc3\xa9dula de ciudadan\xc3\xada'), (b'TI', b'C\xc3\xa9dula de ciudadan\xc3\xada'), (b'CE', b'C\xc3\xa9dula de ciudadan\xc3\xada'), (b'NIT', b'NIT'), (b'PA', b'Pasaporte')], max_length=3, null=True),
        ),
    ]
