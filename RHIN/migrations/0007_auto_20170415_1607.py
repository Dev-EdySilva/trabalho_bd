# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-15 19:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RHIN', '0006_auto_20170415_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=100)),
                ('floor_sal', models.FloatField(default=None)),
                ('flg_active', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'cargo',
            },
        ),
        migrations.AddField(
            model_name='funcionario',
            name='sal',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='cargo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='RHIN.Cargo'),
            preserve_default=False,
        ),
    ]
