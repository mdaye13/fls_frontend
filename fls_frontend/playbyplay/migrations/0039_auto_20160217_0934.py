# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 14:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playbyplay', '0038_playbyplay_eventidx'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PlayerOnIce',
            new_name='PlayerInPlay',
        ),
    ]