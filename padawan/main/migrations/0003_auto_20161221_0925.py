# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-21 14:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20161221_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Ciudad')),
                ('tel_number', models.CharField(blank=True, max_length=25, null=True, verbose_name=b'N\xc3\xbamero telef\xc3\xb3nico')),
                ('email', models.EmailField(blank=True, help_text=b'Si quieres cambiar el correo predeterminado de notificaciones, cambia tu email de cuenta', max_length=254, null=True, verbose_name=b'Correo electr\xc3\xb3nico')),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network', models.CharField(blank=True, choices=[(b'facebook', b'Facebook'), (b'twitter', b'Twitter'), (b'instagram', b'Instagram'), (b'youtube', b'Youtube'), (b'snapchat', b'Snapchat'), (b'pinterest', b'Pinterest'), (b'googleplus', b'Google +')], default=b'facebook', max_length=15, null=True)),
                ('link', models.URLField(blank=True, null=True, verbose_name=b'Enlace a la red social')),
            ],
        ),
        migrations.RemoveField(
            model_name='socialmediasettings',
            name='site',
        ),
        migrations.AlterField(
            model_name='merchantpageslidepicture',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_slide_pictures', to='main.MerchantPage'),
        ),
        migrations.CreateModel(
            name='HomePageRelatedSocialMediaLink',
            fields=[
                ('socialmedialink_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.SocialMediaLink')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_social_media_links', to='main.MerchantPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('main.socialmedialink', models.Model),
        ),
        migrations.DeleteModel(
            name='SocialMediaSettings',
        ),
    ]
