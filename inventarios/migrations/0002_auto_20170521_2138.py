# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-21 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='cantidadProducto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombreProducto',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
