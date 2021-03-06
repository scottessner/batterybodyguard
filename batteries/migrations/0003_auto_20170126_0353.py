# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 03:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('batteries', '0002_auto_20170123_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voltage', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Charger',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('max_cells', models.IntegerField()),
                ('max_current', models.IntegerField()),
                ('parallel_supported', models.BooleanField()),
                ('serial_data_supported', models.BooleanField()),
                ('max_batteries', models.IntegerField()),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='battery',
            name='cell_voltage',
        ),
        migrations.RemoveField(
            model_name='battery',
            name='cells',
        ),
        migrations.AddField(
            model_name='battery',
            name='brand',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='battery',
            name='max_charge_rate',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cell',
            name='battery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='batteries.Battery'),
        ),
    ]
