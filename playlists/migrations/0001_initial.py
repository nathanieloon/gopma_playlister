# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gid', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('last_updated', models.DateTimeField()),
                ('owner', models.CharField(max_length=100)),
                ('share_token', models.CharField(max_length=100)),
            ],
        ),
    ]
