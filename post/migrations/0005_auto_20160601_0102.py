# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 01:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20160527_0113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='fecha',
            new_name='fechacomment',
        ),
    ]
