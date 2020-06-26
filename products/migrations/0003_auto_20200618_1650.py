# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-18 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Pints', 'Pints'), ('Bottles and Cans', 'Bottles/Cans'), ('Soft Drinks', 'Soft-Drinks'), ('Cocktails', 'Cocktails'), ('Spirits', 'Spirits')], default='Pints', max_length=20),
        ),
    ]
