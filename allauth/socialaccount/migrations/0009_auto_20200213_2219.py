# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-14 03:19
from __future__ import unicode_literals

from django.db import migrations
import django_cryptography.fields
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0008_auto_20200209_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='extra_data',
            field=django_cryptography.fields.encrypt(jsonfield.fields.JSONField(default=dict, verbose_name='extra data')),
        ),
    ]
