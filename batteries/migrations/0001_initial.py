# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 07:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cells', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('nickname', models.CharField(max_length=200)),
                ('barcode', models.CharField(max_length=100)),
                ('cell_voltage', models.DecimalField(decimal_places=2, max_digits=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
