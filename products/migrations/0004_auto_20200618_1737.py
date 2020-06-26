# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-18 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200618_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Pints', 'Pints'), ('Bottles and Cans', 'Bottles-Cans'), ('Soft Drinks', 'Soft-Drinks'), ('Cocktails', 'Cocktails'), ('Spirits', 'Spirits')], default='Pints', max_length=20),
        ),
    ]