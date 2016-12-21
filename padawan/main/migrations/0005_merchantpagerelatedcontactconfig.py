# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-21 14:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20161221_0926'),
    ]

    operations = [
        migrations.CreateModel(
            name='MerchantPageRelatedContactConfig',
            fields=[
                ('contactconfig_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.ContactConfig')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_contact_config', to='main.MerchantPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('main.contactconfig', models.Model),
        ),
    ]