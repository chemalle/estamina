# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-11 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounting',
            name='valorReais',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10000),
        ),
    ]