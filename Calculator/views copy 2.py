from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from .models import Variables
from .forms import UserForm, VariablesForm, ExpensesForm, VariablesFormOne, VariablesFormTwo
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User



def user_type(request):
	user_type = 0
	if request.method == "POST":
		user_type = request.POST.get('user_type', '0')
		return user_register(request)
	return render(request, 'Calculator/type.html')

def user_register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return render(request, 'Calculator/accept.html')

    context = {
        "form": form,
    }
    return render(request, 'Calculator/register.html', context)

def user_accept(request):
	if not request.user.is_authenticated():
		return render(request, "Calculator/login.html")
	if request.method == "POST":
		accept = request.POST.get('accept', "")
		if accept == 'accept':
		    return index(request)

	return render(request, "Calculator/accept.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                try:
                	variables = Variables.objects.get(user=user)
                except(ObjectDoesNotExist):
                	User.objects.get(username=username).delete()
                	return user_register(request)

                request.user = user
                context = {
                    "variables": variables,
                    "variable_list":VariablesForm.Meta.fields,
                }
                return render(request, 'Calculator/index.html', context)
            return render(request, 'Calculator/login.html', {'error_message': 'Your account has been disabled'})
        return render(request, 'Calculator/login.html', {'error_message': 'Invalid login'})
    return render(request, 'Calculator/login.html')

def user_logout(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'Calculator/login.html', context)



def index(request):
    if not request.user.is_authenticated():
        return render(request, "Calculator/login.html")

    try:
    	variables = Variables.objects.get(user=request.user.id)	

    except(ObjectDoesNotExist, TypeError):
    	variables = Variables(user=request.user, client_type=user_type)
    	variables.save()

    if request.method == "POST":
        for i in VariablesForm.Meta.fields:
            variable_update = request.POST.get(i, getattr(variables, i))
            if variable_update == "":
                variable_update = 0;
            setattr(variables, i, variable_update)
            variables.save()

    variables = calculate(request, variables)

    context_one = {
        "variables": variables,
        "variable_list":VariablesFormOne.Meta.fields,
    }

    context_two = {
    	"variables": variables,
        "variable_list":VariablesFormTwo.Meta.fields,
    }

    context_three = {
    	"variables": variables,
        "variable_list":VariablesForm.Meta.fields,
    }

    if int(variables.client_type) == 0:
    	return render(request, "Calculator/index.html" , context_one)
    if int(variables.client_type) == 1:
    	return render(request, "Calculator/index.html" , context_two)
    return render(request, "Calculator/index.html" , context_three)


def calculate(request, variables):
    expenses = 0
    for i in ExpensesForm.Meta.fields:
        expenses += float(getattr(variables, i))

    try:
        variables.monthly_income = "%.2f" % (float(variables.goal_income)/(12*float(variables.years_to_achieve))+expenses)
        variables.monthly_extra_income = "%.2f" % (float(variables.monthly_income) - float(variables.personal_income) - float(variables.family_income) - float(variables.other_income))
    except(ZeroDivisionError):
        variables.monthly_income = 0
        variables.monthly_extra_income = 0

    if float(variables.monthly_extra_income) < 0:
        variables.monthly_extra_income = 0
    
    variables.save()
    return variables


    

    

'''
def pie_chart(request):
	ds = DataPool(
       series=
        [{'options': {
            'source': Variables.objects.all()},
          'terms': [
            'month',
            'boston_temp']}
         ])

	cht = Chart(
        datasource = ds, 
        series_options = 
          [{'options':{
              'type': 'pie',
              'stacking': False},
            'terms':{
              'month': [
                'boston_temp']
              }}],
        chart_options = 
          {'title': {
               'text': 'Expense '}},
        x_sortf_mapf_mts = (None, monthname, False))



def monthname(month_num):
    names ={1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
            7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    return names[month_num]
'''

 health_insurance_satisfaction = models.CharField(max_length=100, default="")
    dental_insurance_satisfaction = models.CharField(max_length=100, default="")
    car_insurance_satisfaction = models.CharField(max_length=100, default="")
    house_insurance_satisfaction = models.CharField(max_length=100, default="")
    life_insurance_satisfaction = models.CharField(max_length=100, default="")
    cable_insurance_satisfaction = models.CharField(max_length=100, default="")
    phone_insurance_satisfaction = models.CharField(max_length=100, default="")

    health_insurance_provider = models.CharField(max_length=100, default="")
    dental_insurance_provider = models.CharField(max_length=100, default="")
    car_insurance_provider = models.CharField(max_length=100, default="")
    house_insurance_provider = models.CharField(max_length=100, default="")
    life_insurance_provider = models.CharField(max_length=100, default="")
    cable_insurance_provider = models.CharField(max_length=100, default="")
    phone_insurance_provider = models.CharField(max_length=100, default="")

    boolean_car_purchase_plan = models.BooleanField(default=True)
    boolean_home_finance_plan = models.BooleanField(default=True)
    boolean_college_loan_plan = models.BooleanField(default=True)
    boolean_children_plan = models.BooleanField(default=True)
    boolean_marriage_plan = models.BooleanField(default=True)
    boolean_start_business_plan = models.BooleanField(default=True)
    booelan_other_purchase_plan = models.BooleanField(default=True)

    percentage_of_income_to_save = models.CharField(max_length=100, default="")
    spending_consideration = models.CharField(max_length=100, default="")
    financial_change_speed = models.CharField(max_length=100, default="")
    financial_knowledge = models.CharField(max_length=100, default="")
    investment_interested = models.CharField(max_length=100, default="")
    vacation_plan = models.CharField(max_length=100, default="")


		


