# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roots', '0003_auto_20160201_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portraits',
            name='photo',
            field=models.ImageField(default='image.jpeg', upload_to='/images'),
        ),
    ]
