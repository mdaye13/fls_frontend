# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playbyplay', '0033_auto_20160208_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='season',
            field=models.IntegerField(db_index=True),
        ),
    ]
