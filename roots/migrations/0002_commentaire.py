# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('roots', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('texte', models.TextField()),
                ('date_creation', models.DateTimeField(default=django.utils.timezone.now)),
                ('approuve', models.BooleanField(default=False)),
                ('auteur', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(to='roots.Portraits', related_name='comments')),
            ],
        ),
    ]
