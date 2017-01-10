from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from .models import Variables
from .forms import UserForm, VariablesForm, ExpensesForm


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


def index(request):
    if not request.user.is_authenticated():
        return render(request, "Calculator/login.html")

    variables = Variables.objects.get(user=request.user)

    if request.method == "POST":
        for i in VariablesForm.Meta.fields:
            variable_update = request.POST.get(i, getattr(variables, i))
            if variable_update == "":
                variable_update = 0;
            setattr(variables, i, variable_update)
            variables.save()

    variables = calculate(request, variables)

    context = {
        "variables": variables,
        "variable_list":VariablesForm.Meta.fields,
    }
    return render(request, "Calculator/index.html" , context)

def user_accept(request, user):
	if not request.user.is_authenticated():
		return render(request, "Calculator/login.html")

	if request.method == "POST":
	    accept = request.POST.get('accept', "")
        if accept == "accept":
            return render(request, "Calculator/index.html")
    return render(request, "Calculator/accept.html")





def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                variables = Variables.objects.get(user=user)
                context = {
                    "variables": variables,
                    "variable_list":VariablesForm.Meta.fields,
                }
                return render(request, 'Calculator/index.html', context)
            return render(request, 'Calculator/login.html', {'error_message': 'Your account has been disabled'})
        return render(request, 'Calculator/login.html', {'error_message': 'Invalid login'})
    return render(request, 'Calculator/login.html')


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

                inital_variables = Variables(user=user)
                inital_variables.save()

                return render(request, 'Calculator/index.html', {'variables': inital_variables})
    context = {
        "form": form,
    }
    return render(request, 'Calculator/register.html', context)

def user_logout(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'Calculator/login.html', context)


		


