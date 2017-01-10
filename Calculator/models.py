from django.contrib.auth.models import Permission, User
from django.db import models

class Variables(models.Model):
    user = models.ForeignKey(User, default=1)
    client_type = models.IntegerField(default=0)

    # Results
    monthly_income = models.FloatField(max_length=100000000, default=0)
    monthly_extra_income = models.FloatField(max_length=100000000, default=0)
    monthly_savings  = models.FloatField(max_length=100000000, default=0)

    # Goals
    goal_income = models.FloatField(max_length=100000000, default=0)
    years_to_achieve = models.FloatField(max_length=100000000, default=1)

    # Income
    personal_income = models.FloatField(max_length=100000000, default=0)
    family_income = models.FloatField(max_length=100000000, default=0)
    other_income = models.FloatField(max_length=100000000, default=0)

    # Rent
    house_rent = models.FloatField(max_length=100000000, default=0)
    house_utility = models.FloatField(max_length=100000000, default=0)
    house_misc = models.FloatField(max_length=100000000, default=0)

    # Car
    car_rent = models.FloatField(max_length=100000000, default=0)
    car_miles = models.FloatField(max_length=100000000, default=0)
    car_insurance = models.FloatField(max_length=100000000, default=0)

    #Phone
    phone_rent = models.FloatField(max_length=100000000, default=0)
    phone_usage = models.FloatField(max_length=100000000, default=0)
    phone_insurance = models.FloatField(max_length=100000000, default=0)

    #Cable
    cable_rent = models.FloatField(max_length=100000000, default=0)
    cable_speed = models.FloatField(max_length=100000000, default=0)
    cable_space = models.FloatField(max_length=100000000, default=0)

    #Subscriptions
    phone_subscriptions = models.FloatField(max_length=100000000, default=0)
    computer_subscriptions = models.FloatField(max_length=100000000, default=0)
    other_subscriptions = models.FloatField(max_length=100000000, default=0)

    #Loan
    medical_loan = models.FloatField(max_length=100000000, default=0)
    car_loan = models.FloatField(max_length=100000000, default=0)
    college_loan = models.FloatField(max_length=100000000, default=0)
    house_loan = models.FloatField(max_length=100000000, default=0)
    credit_card_loan = models.FloatField(max_length=100000000, default=0)
    misc_loan = models.FloatField(max_length=100000000, default=0)

    #Vitals
    family_expenses = models.FloatField(max_length=100000000, default=0)
    medical_expenses = models.FloatField(max_length=100000000, default=0)
    dental_expenses = models.FloatField(max_length=100000000, default=0)
    college_expenses = models.FloatField(max_length=100000000, default=0)
    grocery_expenses = models.FloatField(max_length=100000000, default=0)
    cloth_expesnses = models.FloatField(max_length=100000000, default=0)
    life_insurance_expenses = models.FloatField(max_length=100000000, default=0)
    misc_expenses = models.FloatField(max_length=100000000, default=0)

    def __str__(self):
        return str(self.user.username) +"    " + str(self.client_type)






