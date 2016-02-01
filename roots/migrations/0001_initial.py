# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Portraits',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('date_naissance', models.DateField()),
                ('date_mort', models.DateField(null=True)),
                ('description', models.TextField()),
                ('faits', models.TextField()),
                ('fonctions', models.TextField()),
                ('oeuvres', models.TextField()),
                ('date_publication', models.DateTimeField(default=django.utils.timezone.now)),
                ('ajouteePar', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
