# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-06 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_auto_20160206_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='shootsCatches',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
