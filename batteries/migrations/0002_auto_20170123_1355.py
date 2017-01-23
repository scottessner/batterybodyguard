# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 19:55
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('batteries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battery',
            name='barcode',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='battery',
            name='capacity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='battery',
            name='cells',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='battery',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
