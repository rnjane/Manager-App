from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import status
from . import forms, user_auth, budget_models


def index(request):
    return redirect('view_budget_models')


def display_register_page(request):
    return render(request, 'register.html')


def perform_register(request):
    form = forms.UserForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'user account created!')
        return redirect('display-login')
    else:
        messages.error(request, form.errors)
        return redirect('display-register')


def display_login_page(request):
    return render(request, 'login.html')


def perform_login(request):
    form = forms.UserLoginForm(request.POST)
    if form.is_valid():
        response = user_auth.UserAuth().login(username=form.cleaned_data.get(
            'username'), password=form.cleaned_data.get('password'))
        if response.status_code == status.HTTP_200_OK:
            messages.success(request, response.data['message'])
            return redirect('view-money-models')
        messages.error(request, response.data['message'])
        return redirect('display-login')
    messages.error(request, form.errors)
    return redirect('display-login')


@login_required
def view_time_dashboard(request):
    return render(request, 'time-dashboard.html')


@login_required
def view_money_models(request):
    return render(request, 'budget-models.html')


@login_required
def view_time_models(request):
    return render(request, 'time-models.html')


@login_required
def budget_model_details(request, model_budget_id):
    return render(request, 'budget-model-details.html', {'model_budget_id': model_budget_id})


@login_required
def create_budget_model(request):
    form = forms.ModelBudgetForm(request.POST)
    if form.is_valid():
        budget_model_name = form.cleaned_data['budget_model_name']
        response = budget_models.create_budget(
            request=request, name=budget_model_name)
        if response.status_code == status.HTTP_406_NOT_ACCEPTABLE:
            messages.error(request, response.data['message'])
            return redirect('view_money_models')
        else:
            messages.success(request, 'budget model succesfully created')
            return redirect('budget_model_details', response.data['new_budget'].id)
    messages.error(request, form.errors)
    return redirect('view_money_models')


@login_required
def view_budget_models(request):
    my_budget_models = budget_models.view_model_budgets(request)
    return render(request, 'budget-models.html', {'budget_models': my_budget_models.data['budget_models']})


@login_required
def create_model_budget_income(request, model_budget_id):
    '''view to create a new model budget income'''
    form = forms.ModelIncomeForm(request.POST)
    if form.is_valid():
        model_income_name = form.cleaned_data['model_income_name']
        model_income_amount = form.cleaned_data['model_income_amount']
        response = budget_models.create_budget_model_income(
            request=request, amount=model_income_amount, name=model_income_name, model_budget_id=model_budget_id)
        if response.status_code == status.HTTP_406_NOT_ACCEPTABLE:
            messages.error(request, response.data['message'])
            return redirect('budget_model_details', model_budget_id=model_budget_id)
        messages.success(request, response.data['message'])
        return redirect('budget_model_details', model_budget_id=model_budget_id)
