# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-14 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calculator', '0008_auto_20170106_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='variables',
            name='age_date',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='variables',
            name='age_month',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='variables',
            name='age_year',
            field=models.IntegerField(default=2017),
        ),
        migrations.AddField(
            model_name='variables',
            name='boolean_bank_account',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='variables',
            name='boolean_car',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='variables',
            name='boolean_children',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='variables',
            name='boolean_colledge_loan',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='variables',
            name='boolean_credit_cards',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='variables',
            name='boolean_home',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='variables',
            name='boolean_medical_debt',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='variables',
            name='education',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='financial_knowledge',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='variables',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='martial_status',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='phone_number',
            field=models.IntegerField(default=1000000000),
        ),
        migrations.AddField(
            model_name='variables',
            name='sex',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='zip_code',
            field=models.IntegerField(default=10000),
        ),
    ]
