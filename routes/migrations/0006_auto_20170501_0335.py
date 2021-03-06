# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-01 03:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0005_auto_20170501_0200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area',
            old_name='areas_text',
            new_name='area',
        ),
        migrations.RenameField(
            model_name='area',
            old_name='location_text',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='comments_text',
            new_name='comments',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='location_text',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='rating_text',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='routes_text',
            new_name='route_name',
        ),
    ]
