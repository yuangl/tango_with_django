from django.contrib.auth.models import Permission, User
from django.db import models

class Variables(models.Model):
    user = models.ForeignKey(User, default=1)
    client_type = models.IntegerField(default=0)
    #enable_pages = models.BooleanField(default=False)
    enabled = models.BooleanField(default=False)
    key = models.CharField(max_length=100, default="")

    #questionnaire
    last_name = models.CharField(max_length=100, default="")
    first_name = models.CharField(max_length=100, default="")
    zip_code = models.IntegerField(default=10000)
    phone_number = models.IntegerField(default=1000000000)
    age = models.CharField(max_length=100, default="")
    sex = models.CharField(max_length=100, default="")
    martial_status = models.CharField(max_length=100, default="")
    education = models.CharField(max_length=100, default="") 
    financial_knowledge = models.CharField(max_length=100, default="")  
    
    boolean_bank_account = models.BooleanField(default=True)
    boolean_car = models.BooleanField(default=True)
    boolean_home = models.BooleanField(default=True)
    boolean_children = models.BooleanField(default=True)
    boolean_credit_cards = models.BooleanField(default=True)
    boolean_college_loan = models.BooleanField(default=True)
    boolean_medical_debt = models.BooleanField(default=True)

    #Income questions
    have_job = models.CharField(max_length=100, default="No")
    work_length =  models.CharField(max_length=100, default="1-2 years")
    job_title = models.CharField(max_length=100, default="N/A")

    #Rent questions:
    mortgage_satisfaction = models.CharField(max_length=100, default="No")
    mortgage_provider = models.CharField(max_length=100, default="Other")

    #Car questions:
    have_car_loan = models.CharField(max_length=100, default="No")
    car_loan_provider = models.CharField(max_length=100, default="Other")
    car_satisfaction = models.CharField(max_length=100, default="No")
    car_insurance_satisfaction = models.CharField(max_length=100, default="No")
    car_insurance_provider =  models.CharField(max_length=100, default="Other")

    #Phone questions:
    phone_length = models.CharField(max_length=100, default="1-2 years")
    phone_provider = models.CharField(max_length=100, default="Other")
    phone_satisfaction = models.CharField(max_length=100, default="No")

    #Cable questions:
    cable_provider = models.CharField(max_length=100, default="Other")
    cable_satisfaction = models.CharField(max_length=100, default="No")

    #Subscription questions:
    gym_provider = models.CharField(max_length=100, default="Other")

    boolean_netflix = models.BooleanField(default=False)
    boolean_youtube_red = models.BooleanField(default=False)
    boolean_xbox_live = models.BooleanField(default=False)
    boolean_playstation_live = models.BooleanField(default=False)
    boolean_wow = models.BooleanField(default=False)
    boolean_lol = models.BooleanField(default=False)

    #Health insurance questions:
    health_insurance_provider = models.CharField(max_length=100, default="Other")
    health_insurance_satisfaction = models.CharField(max_length=100, default="No")

    #Dental Insurance questions:
    dental_insurance_provider = models.CharField(max_length=100, default="Other")
    dental_insurance_satisfaction = models.CharField(max_length=100, default="No")

    #Debts questions:
    student_loan_manageable = models.CharField(max_length=100, default="No")
    car_loan_manageable = models.CharField(max_length=100, default="No")
    mortgage_manageable = models.CharField(max_length=100, default="No")

    #Vitals questions:
    change_expense_habit =  models.CharField(max_length=100, default="Very Little")

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

class Evaluations(models.Model):
    user = models.ForeignKey(User, default=1)
    client_evaluated = models.BooleanField(default=False)
    client_level = models.IntegerField(default=1)
    client_action_level = models.IntegerField(default=1)

    raise_cloth = models.BooleanField(default=False)
    cloth_urgent = models.BooleanField(default=False)
    cloth_evaluation = models.TextField(max_length=100, default="")

    raise_food = models.BooleanField(default=False)
    food_urgent = models.BooleanField(default=False)
    food_evaluation = models.TextField(max_length=100, default="")

    raise_education = models.BooleanField(default=False)
    education_urgent = models.BooleanField(default=False)
    education_evaluation = models.TextField(max_length=100, default="")

    raise_gym = models.BooleanField(default=False)
    gym_urgent = models.BooleanField(default=False)
    gym_evaluation = models.TextField(max_length=100, default="")

    raise_savings = models.BooleanField(default=False)
    savings_urgent = models.BooleanField(default=False)
    savings_evaluation = models.TextField(max_length=100, default="")

    raise_house = models.BooleanField(default=False)
    house_urgent = models.BooleanField(default=False)
    house_evaluation = models.TextField(max_length=100, default="")

    raise_car = models.BooleanField(default=False)
    car_urgent = models.BooleanField(default=False)
    car_evaluation = models.TextField(max_length=100, default="")

    raise_car_insurance = models.BooleanField(default=False)
    car_insurance_urgent = models.BooleanField(default=False)
    car_insurance_evaluation = models.TextField(max_length=100, default="")

    raise_gas = models.BooleanField(default=False)
    gas_urgent = models.BooleanField(default=False)
    gas_evaluation = models.TextField(max_length=100, default="")

    raise_phone = models.BooleanField(default=False)
    phone_urgent = models.BooleanField(default=False)
    phone_evaluation = models.TextField(max_length=100, default="")

    raise_cable = models.BooleanField(default=False)
    cable_urgent = models.BooleanField(default=False)
    cable_evaluation = models.TextField(max_length=100, default="")

    raise_health_insurance = models.BooleanField(default=False)
    health_insurance_urgent = models.BooleanField(default=False)
    health_insurance_evaluation = models.TextField(max_length=100, default="")

    raise_dental_insurance = models.BooleanField(default=False)
    dental_insurance_urgent = models.BooleanField(default=False)
    dental_insurance_evaluation = models.TextField(max_length=100, default="")

    raise_credit_card = models.BooleanField(default=False)
    credit_card_urgent = models.BooleanField(default=False)
    credit_card_evaluation = models.TextField(max_length=100, default="")

    raise_debt = models.BooleanField(default=False)
    debt_urgent = models.BooleanField(default=False)
    debt_evaluation = models.TextField(max_length=100, default="")

    raise_income = models.BooleanField(default=False)
    income_urgent = models.BooleanField(default=False)
    income_evaluation = models.TextField(max_length=100, default="")
    
    raise_expenses = models.BooleanField(default=False)
    expenses_urgent = models.BooleanField(default=False)
    expenses_evaluation = models.TextField(max_length=100, default="")

    monthly_objectives = models.FloatField(max_length=100000000, default=0)
    yearly_objectives = models.FloatField(max_length=100000000, default=0)
    
    def __str__(self):
        return str(self.user.username) +"    " + str(self.client_evaluated)


class Webinars(models.Model):
    webinar_name = models.CharField(max_length=100, default="")
    webinar_url = models.CharField(max_length=100000000, default="")
    webinar_speaker = models.CharField(max_length=100000000, default="")
    webinar_description = models.TextField(max_length=1000, default="")

    webinar_year = models.CharField(max_length=4, default="")
    webinar_month = models.CharField(max_length=2, default="")
    webinar_month_name = models.CharField(max_length=3, default="")
    webinar_date_of_month = models.CharField(max_length=2, default="")
    webinar_day_of_week = models.CharField(max_length=9, default="")
    webinar_time = models.CharField(max_length=10, default="")

    def __str__(self):
        return str(self.webinar_month)+"/"+ str(self.webinar_date_of_month)+"/"+str(self.webinar_year)+"    "+str(self.webinar_name)

class News(models.Model):
    income_value = models.FloatField(max_length=100000000, default=0)
    gas_value = models.FloatField(max_length=100000000, default=0)
    credit_card_value = models.FloatField(max_length=100000000, default=0)
    mortgage_value = models.FloatField(max_length=100000000, default=0)
    credit_score_value = models.FloatField(max_length=100000000, default=0)
    cell_phone_value = models.FloatField(max_length=100000000, default=0)

    income_rate = models.FloatField(max_length=100000000, default=0)
    gas_rate = models.FloatField(max_length=100000000, default=0)
    credit_card_rate = models.FloatField(max_length=100000000, default=0)
    mortgage_rate = models.FloatField(max_length=100000000, default=0)
    credit_score_rate = models.FloatField(max_length=100000000, default=0)
    cell_phone_rate = models.FloatField(max_length=100000000, default=0)

    income_description =models.TextField(max_length=1000, default="")
    gas_description = models.TextField(max_length=1000, default="")
    credit_card_description = models.TextField(max_length=1000, default="")
    mortgage_description = models.TextField(max_length=1000, default="")
    credit_score_description = models.TextField(max_length=1000, default="")
    cell_phone_description = models.TextField(max_length=1000, default="")

    income_logo = models.CharField(max_length=100000000, default="")
    gas_logo = models.CharField(max_length=100000000, default="")
    credit_card_logo = models.CharField(max_length=100000000, default="")
    mortgage_logo = models.CharField(max_length=100000000, default="")
    credit_score_logo = models.CharField(max_length=100000000, default="")
    cell_phone_logo = models.CharField(max_length=100000000, default="")

    income_url = models.CharField(max_length=100000000, default="")
    gas_url = models.CharField(max_length=100000000, default="")
    credit_card_url = models.CharField(max_length=100000000, default="")
    mortgage_url = models.CharField(max_length=100000000, default="")
    credit_score_url = models.CharField(max_length=100000000, default="")
    cell_phone_url = models.CharField(max_length=100000000, default="")

    def __str__(self):
        return "Ecomonic News Data"








