# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-12 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calculator', '0005_auto_20161212_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variables',
            name='years_to_achieve',
            field=models.FloatField(default=1, max_length=100000000),
        ),
    ]
