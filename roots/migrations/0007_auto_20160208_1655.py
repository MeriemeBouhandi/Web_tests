# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-08 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roots', '0006_auto_20160201_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='adresse_mail',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='prenom',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='pseudo',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='image.jpeg', upload_to='images/'),
        ),
    ]
