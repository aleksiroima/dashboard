# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-27 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='busscheduletable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=10)),
                ('loadtime', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'bus_schedule_table',
            },
        ),
        migrations.CreateModel(
            name='headlinetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('loadtime', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'headline_table',
            },
        ),
        migrations.CreateModel(
            name='sensehattable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('measuretime', models.CharField(max_length=20)),
                ('loadtime', models.CharField(max_length=17)),
            ],
            options={
                'db_table': 'sense_hat_table',
            },
        ),
        migrations.CreateModel(
            name='weathertable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rf_temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('icon_code', models.CharField(max_length=10)),
                ('weather_type', models.CharField(max_length=50)),
                ('forecast_type', models.CharField(max_length=8)),
                ('loadtime', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'weather_table',
            },
        ),
    ]
