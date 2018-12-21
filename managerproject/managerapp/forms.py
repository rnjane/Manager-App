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

class ModelExpenseForm(forms.ModelForm):
    class Meta:
        model = models.ModelExpense
        fields = ['model_expense_name', 'model_expense_amount']


class BudgetForm(forms.ModelForm):
    class Meta:
        model = models.Budget
        fields = ['name']


class IncomeForm(forms.ModelForm):
    class Meta:
        model = models.BudgetIncome
        fields = ['name', 'amount', 'category']


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = models.BudgetExpense
        fields = ['name', 'amount', 'category']


class TimeModelForm(forms.ModelForm):
    class Meta:
        model = models.TimeModel
        fields = ['time_model_name']


class TimeSlotForm(forms.Form):
    model_time_slot_name = forms.CharField(max_length=30)
    hours = forms.IntegerField()
    minutes = forms.IntegerField()
    weekday = forms.CharField(max_length=30)


class ScheduledDayForm(forms.ModelForm):
    class Meta:
        model = models.ScheduledDay
        fields = ['name']