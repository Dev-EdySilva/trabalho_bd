# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-28 18:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RHIN', '0022_auto_20170428_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='funcionario',
        ),
    ]
