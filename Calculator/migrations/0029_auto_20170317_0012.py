# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-17 00:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Calculator', '0028_auto_20170317_0008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variables',
            old_name='health_insruance_satisfaction',
            new_name='health_insurance_satisfaction',
        ),
    ]
