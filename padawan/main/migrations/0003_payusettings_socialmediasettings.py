# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0030_index_on_pagerevision_created_at'),
        ('main', '0002_auto_20161202_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayUSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_id', models.CharField(help_text=b'Tu id de comercio de PayU', max_length=255)),
                ('account_id', models.CharField(help_text=b'Tu id de cuenta de PayU', max_length=255)),
                ('api_login', models.CharField(help_text=b'API login de integraci\xc3\xb3n', max_length=255)),
                ('api_key', models.CharField(help_text=b'API Key de integraci\xc3\xb3n', max_length=255)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Configuraciones PayU',
            },
        ),
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(help_text=b'URl a tu p\xc3\xa1gina de Facebook')),
                ('instagram', models.CharField(help_text=b'Tu usuario de Instagram, sin el @', max_length=255)),
                ('twitter', models.CharField(help_text=b'Tu usuario de Twitter, sin el @', max_length=255)),
                ('youtube', models.URLField(help_text=b'URL a tu canal de Youtube')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Cuentas de redes sociales',
            },
        ),
    ]
