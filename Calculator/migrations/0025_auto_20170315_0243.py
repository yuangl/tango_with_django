# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-15 02:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calculator', '0024_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variables',
            name='booelan_other_purchase_plan',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='boolean_car_purchase_plan',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='boolean_children_plan',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='boolean_college_loan_plan',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='boolean_home_finance_plan',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='boolean_marriage_plan',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='boolean_start_business_plan',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='cable_insurance_provider',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='cable_insurance_satisfaction',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='car_insurance_provider',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='dental_insurance_satisfaction',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='financial_change_speed',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='financial_knowledge',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='health_insurance_satisfaction',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='house_insurance_provider',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='house_insurance_satisfaction',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='investment_interested',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='life_insurance_provider',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='life_insurance_satisfaction',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='percentage_of_income_to_save',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='phone_insurance_provider',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='phone_insurance_satisfaction',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='spending_consideration',
        ),
        migrations.RemoveField(
            model_name='variables',
            name='vacation_plan',
        ),
        migrations.AddField(
            model_name='variables',
            name='cable_provider',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='cable_satisfaction',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='car_insruance_provider',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='car_loan_manageable',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='car_loan_provider',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='car_satisfaction',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='change_expense_habit',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='have_car_loan',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='have_job',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='health_insruance_satisfaction',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='job_title',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='mortgage_manageable',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='mortgage_provider',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='mortgage_satisfaction',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='phone_length',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='phone_provider',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='phone_satisfaction',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='student_loan_manageable',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='variables',
            name='work_length',
            field=models.CharField(default='', max_length=100),
        ),
    ]
