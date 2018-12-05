from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models

class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=50)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(max_length=100)

class ModelBudgetForm(forms.ModelForm):
    class Meta:
        model = models.BudgetModel
        fields = ['budget_model_name']


class ModelIncomeForm(forms.ModelForm):
    class Meta:
        model = models.ModelIncome
        fields = ['model_income_name', 'model_income_amount']