from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from .models import Variables
from .forms import UserForm, VariablesForm, ExpensesForm, VariablesFormOne, VariablesFormTwo
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

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
                return context_return(request, variables)
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
                return user_accept(request)
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
            return render(request, 'Calculator/type.html')
    return render(request, "Calculator/accept.html")

def user_type(request):
    if not request.user.is_authenticated():
        return render(request, "Calculator/login.html")
    if request.method == "POST":
        client = request.POST['options']
        return index(request, client)
    return render(request, 'Calculator/type.html')

def index(request, client):
    if not request.user.is_authenticated():
        return render(request, "Calculator/login.html")
    user = request.user
    try:
        variables = Variables.objects.get(user=user)
    except Variables.DoesNotExist:
        variables = Variables(user=user, client_type = client)
        variables.save()
    if request.method == "POST":
        for i in VariablesForm.Meta.fields:
            variable_update = request.POST.get(i, getattr(variables, i))
            if variable_update == "":
                variable_update = 0;
            setattr(variables, i, variable_update)
            variables.save()
    variables = calculate(request, variables)
    return context_return(request, variables)


def context_return(request, variables):
    variable_names = [  'Monthly Ideal Savings',
                        'Monthly Extra Income',
                        'Monthly Real Savings',
                  
                        'Goal Savings',
                        'Years to Achieve',

                        'Job/Work', 
                        'Family/Friends', 
                        'Other Income',

                        'Payments Per Month',
                        'Water/Gas/Electricity',
                        'Misc. Expenses',

                        'Payment Per Month',
                        'Average Miles Per Week',
                        'Car Insurance',

                        'Payment per month',
                        'Gigs used per month',
                        'Protection Plan',

                        'Payment Per Month',
                        'Speed provided',
                        'Space/Size Data/Package',

                        'Phone Subscriptions',
                        'Computer Subscriptions',
                        'Other Subscriptions',
                        
                        'Medical Debt',
                        'Car Loan',
                        'Student Loans',
                        'Mortgage',
                        'Credit Card Debt',
                        'Misc. Loans/Debts',

                        'Family Expenses',
                        'Medical Expenses',
                        'Dental Expenses',
                        'College Expenses',
                        'Groceries/Food/Water',
                        'Clothes/Accessories',
                        'Life Insurance Expenses',
                        'Misc. Expenses']


    variable_descriptions = ['monthly_income_descriptions',
                        'monthly_extra_income_descriptions',
                        'monthly_savings_descriptions',
                  
                        'How much you wish to save',
                        'How many years to achieve',

                        'Monthly income from all jobs/work done', 
                        'Monthly income from all family/friends', 
                        'Monthly income from all other sources not specified',

                        'Monthly payment for rent/mortgage excluding other costs',
                        'Total accumulation of cost for water/gas/electricity per month excluding other costs',
                        'Any other home expense you pay in order to upkeep your property or anything that is related to home maintenance',

                        'Monthly car payment including tax and excluding any other expense',
                        'Average miles driven per week',
                        'Monthly payment on car insurance including tax and excluding another other non-related car expense',

                        'Phone bill payment per month including tax and excluding any other expense',
                        'Estimated amount of gigabytes used per month',
                        'Monthly payment for phone protection plan if applicable',

                        'Monthly payment for cable and Internet service combined',
                        'Amount of speed provided with current plan',
                        'Amount of space/size/data that the service provider provides before additional charges are added ',

                        'Any phone subscriptions you may be paying for such as online apps, music apps, gaming apps, and/or storage apps',
                        'Any computer subscriptions you may be paying for such as online management and entertainment subscriptions',
                        'Any other subscriptions you may be paying for such as newspaper, magazine, and/or water delivery subscriptions, etc.',
                        
                        'All known medical debt owed',
                        'Total amount financed on your car with including all taxes',
                        'Total amount owed to the college, university, or trade school you attended',
                        'Calculate your current mortgage payment or what it would be. Keep in mind the current rates',
                        'Sum up any credit card debt and put it on an affordable monthly payment budget',
                        'May include remaining college debt, business loan debt, etc.',

                        'Total amount of expenses if you have children, helping to support family/friends, etc.',
                        'Total amount for your medical insurance plan (including you and your dependents if applicable)',
                        'Total amount for dental expenses or dental plans (including you and your dependents if applicable)',
                        'Total amount if you and/or your children have college tuition or expenses such as textbooks, supplies, class fees, etc.',
                        'Average amount spent on food, water, and groceries purchased on a monthly basis',
                        'Total expenses on all clothes, shoes, and other wearable accessories that you purchase on a monthly bases.',
                        'Total monthly payment for life insurance for you, your spouse, and/or children if applicable',
                        'Any other expense not specified in any of these categories and would like to enter those amounts']

    table_names =  [    'Results',
                        'Results',
                        'Results',
                  
                        'Goal Achievements',
                        'Goal Achievements',

                        'Income', 
                        'Income', 
                        'Income',

                        'Rent/Mortgage',
                        'Rent/Mortgage',
                        'Rent/Mortgage',

                        'Car Expenses',
                        'Car Expenses',
                        'Car Expenses',

                        'Phone Expenses',
                        'Phone Expenses',
                        'Phone Expenses',

                        'Cable/Internet',
                        'Cable/Internet',
                        'Cable/Internet',

                        'Subscriptions',
                        'Subscriptions',
                        'Subscriptions',
                        
                        'Debt Expenses',
                        'Debt Expenses',
                        'Debt Expenses',
                        'Debt Expenses',
                        'Debt Expenses',
                        'Debt Expenses',

                        'Vitals Expenses',
                        'Vitals Expenses',
                        'Vitals Expenses',
                        'Vitals Expenses',
                        'Vitals Expenses',
                        'Vitals Expenses',
                        'Vitals Expenses',
                        'Vitals Expenses']

    house = float(variables.house_rent) + float(variables.house_utility) + float(variables.house_misc)
    car = float(variables.car_rent) + float(variables.car_insurance)+ float(variables.car_miles)
    phone = float(variables.phone_rent) + float(variables.phone_insurance)
    cable = float(variables.cable_rent)
    subscriptions = float(variables.phone_subscriptions) + float(variables.computer_subscriptions)+ float(variables.other_subscriptions)
    loan = float(variables.medical_loan) + float(variables.car_loan) + float(variables.college_loan) + float(variables.house_loan) + float(variables.credit_card_loan) + float(variables.misc_loan)
    expenses = float(variables.family_expenses) + float(variables.medical_expenses) + float(variables.dental_expenses) + float(variables.college_expenses) + float(variables.grocery_expenses) + float(variables.cloth_expesnses) + float(variables.life_insurance_expenses) + float(variables.misc_expenses)


    context_one = {
        "variables": variables,
        "variable_list":zip(VariablesFormOne.Meta.fields, variable_names[0: len(VariablesFormOne.Meta.fields)], 
                                                          variable_descriptions[0: len(VariablesFormOne.Meta.fields)], 
                                                          table_names[0: len(VariablesFormOne.Meta.fields)] ),
        "client":variables.client_type,
        "house" : house,    
        "car" : car,
        "phone" : phone,
        "cable" : cable,
        "subscriptions" : subscriptions,
        "loan" : loan,
        "expenses": expenses,
        "savings" : variables.monthly_savings,
    }
    context_two = {
        "variables": variables,
        "variable_list":zip(VariablesFormTwo.Meta.fields, variable_names[0: len(VariablesFormTwo.Meta.fields)], 
                                                          variable_descriptions[0: len(VariablesFormTwo.Meta.fields)], 
                                                          table_names[0: len(VariablesFormTwo .Meta.fields)] ),
        "client":variables.client_type,
        "house" : house,    
        "car" : car,
        "phone" : phone,
        "cable" : cable,
        "subscriptions" : subscriptions,
        "loan" : loan,
        "expenses": expenses,
        "savings" : variables.monthly_savings,
    }
    context_three = {
        "variables": variables,
        "variable_list":zip(VariablesForm.Meta.fields, variable_names[0: len(VariablesForm.Meta.fields)], 
                                                       variable_descriptions[0: len(VariablesForm.Meta.fields)], 
                                                       table_names[0: len(VariablesForm.Meta.fields)] ),
        "client":variables.client_type,
        "house" : house,    
        "car" : car,
        "phone" : phone,
        "cable" : cable,
        "subscriptions" : subscriptions,
        "loan" : loan,
        "expenses": expenses,
        "savings" : variables.monthly_savings,
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
        variables.monthly_savings = "%.2f" % (float(variables.personal_income) + float(variables.family_income) + float(variables.other_income) - 
            float(variables.house_rent)
                  -float(variables.house_utility)
                  -float(variables.house_misc)
                
                  -float(variables.car_rent)
                  -float(variables.car_insurance)
                  
                  -float(variables.phone_rent)
                  -float(variables.phone_insurance)                  
                  -float(variables.cable_rent)
                  
                  -float(variables.phone_subscriptions)
                  -float(variables.computer_subscriptions)                  
                  -float(variables.other_subscriptions)         

                  -float(variables.medical_loan)
                  -float(variables.car_loan)               
                  -float(variables.college_loan)
                  -float(variables.house_loan)
                  -float(variables.credit_card_loan)                  
                  -float(variables.misc_loan)
                  
                  -float(variables.family_expenses)
                  -float(variables.medical_expenses)
                  -float(variables.dental_expenses)
                  -float(variables.college_expenses)
                  -float(variables.grocery_expenses)
                  -float(variables.cloth_expesnses)
                  -float(variables.life_insurance_expenses)
                  -float(variables.misc_expenses)
            )
    except(ZeroDivisionError):
        variables.monthly_income = 0
        variables.monthly_extra_income = 0
        variables.monthly_savings = 0
    if float(variables.monthly_extra_income) < 0:
        variables.monthly_extra_income = 0
    variables.save()
    return variables


def user_chart(request):
    if not request.user.is_authenticated():
        return render(request, "Calculator/login.html")
    
    variables = Variables.objects.get(user=request.user)  
    
    house = float(variables.house_rent) + float(variables.house_utility) + float(variables.house_misc)
    car = float(variables.car_rent) + float(variables.car_insurance)+ float(variables.car_miles)
    phone = float(variables.phone_rent) + float(variables.phone_insurance)
    cable = float(variables.cable_rent)
    subscriptions = float(variables.phone_subscriptions) + float(variables.computer_subscriptions)+ float(variables.other_subscriptions)
    loan = float(variables.medical_loan) + float(variables.car_loan) + float(variables.college_loan) + float(variables.house_loan) + float(variables.credit_card_loan) + float(variables.misc_loan)
    expenses = float(variables.family_expenses) + float(variables.medical_expenses) + float(variables.dental_expenses) + float(variables.college_expenses) + float(variables.grocery_expenses) + float(variables.cloth_expesnses) + float(variables.life_insurance_expenses) + float(variables.misc_expenses)
    context = {
        "house" : house,    
        "car" : car,
        "phone" : phone,
        "cable" : cable,
        "subscriptions" : subscriptions,
        "loan" : loan,
        "expenses": expenses,
        "client" : variables.client_type,
        "savings" : variables.monthly_savings,
    }
    return render(request, "Calculator/chart.html", context)








