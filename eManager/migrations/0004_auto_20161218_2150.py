# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-18 21:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eManager', '0003_auto_20161218_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
    ]
