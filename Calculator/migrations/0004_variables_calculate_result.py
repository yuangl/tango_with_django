# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-06 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calculator', '0003_auto_20161202_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='variables',
            name='calculate_result',
            field=models.FloatField(default=0, max_length=100000000),
        ),
    ]
