# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-15 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calculator', '0025_auto_20170315_0243'),
    ]

    operations = [
        migrations.AddField(
            model_name='variables',
            name='financial_knowledge',
            field=models.CharField(default='', max_length=100),
        ),
    ]
