import hashlib #, random, string
import datetime, calendar
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from django.views.generic import View
from django.utils.crypto import get_random_string
from .models import Variables, Webinars, News, Evaluations
from .forms import UserForm, VariablesForm, ExpensesForm, VariablesFormOne, VariablesFormTwo


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
	            login(request, user)

	            try:
	                variables = Variables.objects.get(user=request.user)
	            except(ObjectDoesNotExist):
	                User.objects.get(username=username).delete()
	                return user_register(request)
	            if variables.enabled == True:
	            	#random_key_adder = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for i in range(10))
	            	#variables.key = random_key_adder + variables.key
	            	variables.key = generate_key(username)
	            	variables.save()
	            	return index(request, variables.client_type)
	            return render(request, 'Calculator/questionnaire.html', {"key" : variables.key})
            return render(request, 'Calculator/login.html', {'error_message': 'Your account has been disabled'})
        return render(request, 'Calculator/login.html', {'error_message': 'Invalid login'})
    return render(request, 'Calculator/login.html')


def user_email_address(request):
    if request.method == "POST":
        email = request.POST.get('email_address', "")

        #check for username
        try:
	        user = User.objects.get(username=email)
        except(ObjectDoesNotExist): 
        	return render(request, 'Calculator/error.html')

        try:        
           	variables = Variables.objects.get(user=user)
        except Variables.DoesNotExist:
            variables = Variables(user=user)
            variables.save()

        key = variables.key
        subject = 'Change Password'
        message = 'Please click to change password: http://127.0.0.1:8000/Calculator/reset_password/'+str(key)
        from_email = settings.EMAIL_HOST_USER
        to_list = [email]
        send_mail(subject, message, from_email, to_list, fail_silently=False)

        return render(request, 'Calculator/email.html')
    return render(request, 'Calculator/email_address.html')
 
def user_reset_password(request, key):	
    if request.method == "POST":
        password = request.POST.get('password', "")

        try:        
           	variables = Variables.objects.get(key=key)
        except Variables.DoesNotExist:
            return render(request, 'Calculator/error.html')

        variables.user.set_password(password)
        variables.user.save()
        return render(request, 'Calculator/login.html')
    return render(request, 'Calculator/reset_password.html', {"key": key})

def user_error(request):
	return render(request, 'Calculator/error.html')

def user_register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        
        user.set_password(password)
        user.save()

        key = generate_key(username)
        subject = 'Registration Email'
        message = 'Please click to register: http://127.0.0.1:8000/Calculator/questionnaire/'+str(key)
        from_email = settings.EMAIL_HOST_USER
        to_list = [username]
        send_mail(subject, message, from_email, to_list, fail_silently=False)

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                user = request.user
                try:        
                    variables = Variables.objects.get(user=user)
                    evaluations = Evaluations.objects.get(user=user)
                except Variables.DoesNotExist:
                    variables = Variables(user=user)
                    variables.save()
                    evaluations = Evaluations(user=user)
                    evaluations.save()
                variables.key = key
                variables.save()
                return render(request, 'Calculator/email.html')
    context = {
        "form": form,
    }
    return render(request, 'Calculator/register.html', context)


def generate_key(username):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(20, chars)
    return hashlib.sha256((secret_key + username).encode('utf-8')).hexdigest()


def user_questionnaire(request, key):
    if not request.user.is_authenticated():
        return render(request, "Calculator/login.html")
    user = request.user
    try:        
        variables = Variables.objects.get(user=user)
    except Variables.DoesNotExist:
        variables = Variables(user=user)
        variables.save()
    if request.method == "POST":
        variables.last_name = request.POST.get('last_name', "")
        variables.first_name = request.POST.get('first_name', "")
        variables.zip_code = request.POST.get('zip_code',10000)
        variables.phone_number = request.POST.get('phone_number', 1000000000)
        variables.age = request.POST.get('age',"2017/01/01")
        variables.sex = request.POST.get('sex', "")
        variables.martial_status = request.POST.get('martial_status', "")
        variables.education = request.POST.get('education', "")
        variables.financial_knowledge = request.POST.get('financial_knowledge', "")
        variables.boolean_bank_account = request.POST.get("boolean_bank_account", False)
        variables.boolean_car = request.POST.get("boolean_car", False)
        variables.boolean_home = request.POST.get("boolean_home", False)
        variables.boolean_children = request.POST.get("boolean_children", False)
        variables.boolean_credit_cards = request.POST.get("boolean_credit_cards", False)
        variables.boolean_college_loan = request.POST.get("boolean_college_loan", False)
        variables.boolean_medical_debt = request.POST.get("boolean_medical_debt", False)
        variables.have_job = request.POST.get("have_job", "")
        variables.work_length = request.POST.get("work_length", "")
        variables.job_title = request.POST.get("job_title", "")
        variables.mortgage_satisfaction = request.POST.get("mortgage_satisfaction", "")
        variables.mortgage_provider = request.POST.get("mortgage_provider", "")
        variables.have_car_loan = request.POST.get("have_car_loan", "")
        variables.car_loan_provider = request.POST.get("car_loan_provider", "")
        variables.car_satisfaction = request.POST.get("car_satisfaction", "")
        variables.car_insurance_satisfaction = request.POST.get("car_insurance_satisfaction", "")
        variables.car_insurance_provider =  request.POST.get("car_insurance_provider", "")
        variables.phone_length = request.POST.get("phone_length", "")
        variables.phone_provider = request.POST.get("phone_provider", "")
        variables.phone_satisfaction = request.POST.get("phone_satisfaction", "")
        variables.cable_provider = request.POST.get("cable_provider", "")
        variables.cable_satisfaction = request.POST.get("cable_satisfaction", "")
        variables.gym_provider = request.POST.get("gym_provider", "")
        variables.boolean_netflix = request.POST.get("boolean_netflix", False)
        variables.boolean_youtube_red = request.POST.get("boolean_youtube_red", False)
        variables.boolean_xbox_live = request.POST.get("boolean_xbox_live", False)
        variables.boolean_playstation_live = request.POST.get("boolean_playstation_live", False) 
        variables.boolean_wow = request.POST.get("boolean_wow", False)
        variables.boolean_lol = request.POST.get("boolean_lol", False)
        variables.health_insurance_provider = request.POST.get("health_insurance_provider", "")
        variables.health_insurance_satisfaction = request.POST.get("health_insurance_satisfaction", "")
        variables.dental_insurance_provider = request.POST.get("dental_insurance_provider", "")
        variables.dental_insurance_satisfaction = request.POST.get("dental_insurance_satisfaction", "")
        variables.student_loan_manageable = request.POST.get("student_loan_manageable", "")
        variables.car_loan_manageable = request.POST.get("car_loan_manageable", "")
        variables.mortgage_manageable = request.POST.get("mortgage_manageable", "")
        variables.change_expense_habit = request.POST.get("change_expense_habit", "")
        variables.save()
        return render(request, 'Calculator/accept.html')
    context = {
        "variables": variables,
        "key": key
        }
    return render(request, 'Calculator/questionnaire.html', context)


def user_accept(request):
    if not request.user.is_authenticated():
        return render(request, "Calculator/login.html")
    if request.method == "POST":
        accept = request.POST.get('accept', "")
        if accept == 'accept':
            user = request.user
            try:        
                variables = Variables.objects.get(user=user)
                variables.enabled = True
                variables.save()
            except Variables.DoesNotExist:
                variables = Variables(user=user)
                variables.save()
            return render(request, 'Calculator/type.html')
    return render(request, "Calculator/accept.html")

def user_type(request):
    if not request.user.is_authenticated():
        return render(request, "Calculator/login.html")
    if request.method == "POST":
        client = request.POST.get("client_type", 0)
        user = request.user
        try:        
            variables = Variables.objects.get(user=user)
            variables.client_type = client
            variables.enabled = True
            variables.save()
        except Variables.DoesNotExist:
            variables = Variables(user=user)
            variables.client_type = client
            variables.save()
        return index(request, client)
    return render(request, 'Calculator/type.html')

def index(request, client):
    if not request.user.is_authenticated():
        return render(request, "Calculator/login.html")
    user = request.user
    try:
        variables = Variables.objects.get(user=user)
        variables.client_type = client
        variables.save()
    except Variables.DoesNotExist:
        variables = Variables(user=user, client_type = client)
        variables.save()
    if variables.enabled == False:
        return render(request, "Calculator/questionnaire.html", {"key" : variables.key })
    if request.method == "POST":
        for i in VariablesForm.Meta.fields:
            variable_update = request.POST.get(i, getattr(variables, i))
            if variable_update == "":
                variable_update = 0;
            setattr(variables, i, variable_update)
            variables.save()
    variables = calculate(request, variables)
    return context_return(request, variables)



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
        "variables" : variables,
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
    context_two = {
        "variables": variables,
        "variable_list":zip(VariablesForm.Meta.fields, variable_names[0: len(VariablesForm.Meta.fields)], 
                                                          variable_descriptions[0: len(VariablesForm.Meta.fields)], 
                                                          table_names[0: len(VariablesForm .Meta.fields)] ),
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

def webinar_menu(request):
    if not request.user.is_authenticated():
        return render(request, "Calculator/login.html")
    user = request.user
    try:        
        variables = Variables.objects.get(user=user)
    except Variables.DoesNotExist:
        variables = Variables(user=user)
        variables.save() 
    if variables.enabled == False:
        return render(request, "Calculator/questionnaire.html", {"key" : variables.key })
        
    past_webinars = list()
    upcoming_webinars = list()

    #webinars_list = Webinars.objects.all().order_by("-webinar_time")

    webinars_list = Webinars.objects.all().order_by('webinar_year', 'webinar_month', 'webinar_date_of_month')
    today = datetime.datetime.now().strftime("20%y/%m/%d")

    for webinar in webinars_list:
        webinar_date = str(webinar.webinar_year) + "/" +str(webinar.webinar_month) + "/" + str(webinar.webinar_date_of_month)
        if webinar_date < today:
            past_webinars.insert(0, webinar)
        else:
            upcoming_webinars.append(webinar)
    upcoming_pages = webinars_pagination(request, upcoming_webinars)
    past_pages = webinars_pagination(request, past_webinars)
    context = {
        "variables": variables,
        "upcoming_pages" : upcoming_pages,
        "past_pages" : past_pages,
            }
    return render(request, "Calculator/webinar_menu.html" , context)

def webinars_pagination(request, webinars_list):
    paginator = Paginator(webinars_list, 3)
    page = request.GET.get('page')
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    return pages     

def return_index(request):     
    if not request.user.is_authenticated():
        return render(request, "Calculator/login.html")   
    user = request.user
    try:        
        variables = Variables.objects.get(user=user)
        return index(request, variables.client_type)
    except Variables.DoesNotExist:
        variables = Variables(user=user)
        variables.save()
    if variables.enabled == False:
        return render(request, "Calculator/questionnaire.html", {"key" : variables.key })
    return render(request, 'Calculator/login.html')

def user_infor(request):
    if not request.user.is_authenticated():
        return render(request, "Calculator/login.html")   
    user = request.user
    try:        
        variables = Variables.objects.get(user=user)
    except Variables.DoesNotExist:
        variables = Variables(user=user)
        variables.save()
    if variables.enabled == False:
        return render(request, "Calculator/questionnaire.html", {"key" : variables.key })
    if request.method == "POST":
        variables.last_name = request.POST.get('last_name', "")
        variables.first_name = request.POST.get('first_name', "")
        variables.zip_code = request.POST.get('zip_code',10000)
        variables.phone_number = request.POST.get('phone_number', 1000000000)
        variables.age = request.POST.get('age',"2017/01/01")
        variables.sex = request.POST.get('sex', "")
        variables.martial_status = request.POST.get('martial_status', "")
        variables.education = request.POST.get('education', "")
        variables.financial_knowledge = request.POST.get('financial_knowledge', "")
        variables.boolean_bank_account = request.POST.get("boolean_bank_account", False)
        variables.boolean_car = request.POST.get("boolean_car", False)
        variables.boolean_home = request.POST.get("boolean_home", False)
        variables.boolean_children = request.POST.get("boolean_children", False)
        variables.boolean_credit_cards = request.POST.get("boolean_credit_cards", False)
        variables.boolean_college_loan = request.POST.get("boolean_college_loan", False)
        variables.boolean_medical_debt = request.POST.get("boolean_medical_debt", False)
        variables.have_job = request.POST.get("have_job", "")
        variables.work_length = request.POST.get("work_length", "")
        variables.job_title = request.POST.get("job_title", "")
        variables.mortgage_satisfaction = request.POST.get("mortgage_satisfaction", "")
        variables.mortgage_provider = request.POST.get("mortgage_provider", "")
        variables.have_car_loan = request.POST.get("have_car_loan", "")
        variables.car_loan_provider = request.POST.get("car_loan_provider", "")
        variables.car_satisfaction = request.POST.get("car_satisfaction", "")
        variables.car_insurance_satisfaction = request.POST.get("car_insurance_satisfaction", "")
        variables.car_insurance_provider =  request.POST.get("car_insurance_provider", "")
        variables.phone_length = request.POST.get("phone_length", "")
        variables.phone_provider = request.POST.get("phone_provider", "")
        variables.phone_satisfaction = request.POST.get("phone_satisfaction", "")
        variables.cable_provider = request.POST.get("cable_provider", "")
        variables.cable_satisfaction = request.POST.get("cable_satisfaction", "")
        variables.gym_provider = request.POST.get("gym_provider", "")
        variables.boolean_netflix = request.POST.get("boolean_netflix", False)
        variables.boolean_youtube_red = request.POST.get("boolean_youtube_red", False)
        variables.boolean_xbox_live = request.POST.get("boolean_xbox_live", False)
        variables.boolean_playstation_live = request.POST.get("boolean_playstation_live", False) 
        variables.boolean_wow = request.POST.get("boolean_wow", False)
        variables.boolean_lol = request.POST.get("boolean_lol", False)
        variables.health_insurance_provider = request.POST.get("health_insurance_provider", "")
        variables.health_insurance_satisfaction = request.POST.get("health_insurance_satisfaction", "")
        variables.dental_insurance_provider = request.POST.get("dental_insurance_provider", "")
        variables.dental_insurance_satisfaction = request.POST.get("dental_insurance_satisfaction", "")
        variables.student_loan_manageable = request.POST.get("student_loan_manageable", "")
        variables.car_loan_manageable = request.POST.get("car_loan_manageable", "")
        variables.mortgage_manageable = request.POST.get("mortgage_manageable", "")
        variables.change_expense_habit = request.POST.get("change_expense_habit", "")
        variables.save()
        context = {"variables": variables}
        return render(request, 'Calculator/infor.html', context)
    context = {"variables": variables}
    return render(request, 'Calculator/infor.html', context)

def economic_news(request):
    if not request.user.is_authenticated():
       return render(request, "Calculator/login.html")
    user = request.user
    try:        
        variables = Variables.objects.get(user=user)
    except Variables.DoesNotExist:
        variables = Variables(user=user)
        variables.save() 
    if variables.enabled == False:
        return render(request, "Calculator/questionnaire.html", {"key" : variables.key })
    try:        
        news = News.objects.get(id=1)
    except News.DoesNotExist:
        news = News(id=1)
        news.save()
    context = {
        "economic_news": news,
        "variables": variables,
        }
    return render(request, 'Calculator/news.html', context)

def user_plan(request):
    if not request.user.is_authenticated():
       return render(request, "Calculator/login.html")
    user = request.user
    try:        
        variables = Variables.objects.get(user=user)
    except Variables.DoesNotExist:
        variables = Variables(user=user)
        variables.save() 
    if variables.enabled == False:
        return render(request, "Calculator/questionnaire.html", {"key" : variables.key })
    try:        
        evaluations = Evaluations.objects.get(user=user)
        evaluations.save()
    except Evaluations.DoesNotExist:
        evaluations = Evaluations(user=user)
        evaluations.save()
    context = {
        "evaluations": evaluations,
        "variables": variables,
        }
    return render(request, "Calculator/plan.html", context)

def user_logout(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'Calculator/login.html', context)
'''
def webinar(request):
    if not request.user.is_authenticated():
        return render(request, "Calculator/login.html")

    context = {

    }
    return render(request, "Calculator/webinar.html" , context)
'''




