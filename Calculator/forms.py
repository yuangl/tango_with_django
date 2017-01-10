from django.contrib.auth.models import User
from django import forms
from .models import Variables

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password']


class VariablesForm(forms.ModelForm):

    class Meta:
        model = Variables
        fields = [  'monthly_income',
                    'monthly_extra_income',
                    'monthly_savings',
                  
                    'goal_income',
              			'years_to_achieve',

              			'personal_income', 
              			'family_income', 
              			'other_income',

              			'house_rent',
              			'house_utility',
              			'house_misc',

              			'car_rent',
              			'car_miles',
              			'car_insurance',

              			'phone_rent',
              			'phone_usage',
              			'phone_insurance',

              			'cable_rent',
              			'cable_speed',
              			'cable_space',

              			'phone_subscriptions',
              			'computer_subscriptions',
      					    'other_subscriptions',
              			
              			'medical_loan',
              			'car_loan',
              			'college_loan',
              			'house_loan',
              			'credit_card_loan',
              			'misc_loan',

              			'family_expenses',
              			'medical_expenses',
              			'dental_expenses',
              			'college_expenses',
              			'grocery_expenses',
              			'cloth_expesnses',
              			'life_insurance_expenses',
              			'misc_expenses'
        			]

class VariablesFormOne(forms.ModelForm):

    class Meta:
        model = Variables
        fields = [  'monthly_income',
                    'monthly_extra_income',
                    'monthly_savings',
                  
                    'goal_income',
                    'years_to_achieve',

                    'personal_income', 
                    'family_income', 
                    'other_income',

                    'house_rent',
                    'house_utility',
                    'house_misc',

                    'car_rent',
                    'car_miles',
                    'car_insurance',

                    'phone_rent',
                    'phone_usage',
                    'phone_insurance',

                    'cable_rent',
                    'cable_speed',
                    'cable_space'
              ]

class VariablesFormTwo(forms.ModelForm):

    class Meta:
        model = Variables
        fields = [  'monthly_income',
                    'monthly_extra_income',
                    'monthly_savings',
                  
                    'goal_income',
                    'years_to_achieve',

                    'personal_income', 
                    'family_income', 
                    'other_income',

                    'house_rent',
                    'house_utility',
                    'house_misc',

                    'car_rent',
                    'car_miles',
                    'car_insurance',

                    'phone_rent',
                    'phone_usage',
                    'phone_insurance',

                    'cable_rent',
                    'cable_speed',
                    'cable_space',

                    'phone_subscriptions',
                    'computer_subscriptions',
                    'other_subscriptions',
                    
                    'medical_loan',
                    'car_loan',
                    'college_loan',
                    'house_loan',
                    'credit_card_loan',
                    'misc_loan'
              ]



class ExpensesForm(forms.ModelForm):
    
    class Meta:
        model = Variables
        fields = [
                  'house_rent',
                  'house_utility',
                  'house_misc',
                  
                  'car_rent',
                  'car_insurance',
                  
                  'phone_rent',
                  'phone_insurance',
                  
                  'cable_rent',
                  
                  'phone_subscriptions',
                  'computer_subscriptions',
                  'other_subscriptions',
                  
                  'medical_loan',
                  'car_loan',
                  'college_loan',
                  'house_loan',
                  'credit_card_loan',
                  'misc_loan',
                  
                  'family_expenses',
                  'medical_expenses',
                  'dental_expenses',
                  'college_expenses',
                  'grocery_expenses',
                  'cloth_expesnses',
                  'life_insurance_expenses',
                  'misc_expenses'
                  ]