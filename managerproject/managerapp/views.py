from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import status
from django.shortcuts import get_object_or_404
from . import forms, user_auth, budget_models, models, budgets


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
            return redirect('view_budget_models')
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
def create_budget_model(request):
    form = forms.ModelBudgetForm(request.POST)
    if form.is_valid():
        budget_model_name = form.cleaned_data['budget_model_name']
        response = budget_models.create_budget(
            request=request, name=budget_model_name)
        if response.status_code == status.HTTP_406_NOT_ACCEPTABLE:
            messages.error(request, response.data['message'])
            return redirect('view_budget_models')
        else:
            messages.success(request, 'budget model succesfully created')
            return redirect('budget_model_details', response.data['new_budget'].id)
    messages.error(request, form.errors)
    return redirect('view_budget_models')


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
            request=request, amount=model_income_amount, name=model_income_name, budget_id=model_budget_id)
        if response.status_code == status.HTTP_201_CREATED:
            messages.success(request, response.data['message'])
            return redirect('budget_model_details', model_budget_id=model_budget_id)
        messages.error(request, response.data['message'])
        return redirect('budget_model_details', model_budget_id=model_budget_id)
    messages.error(request, form.errors)
    return redirect('budget_model_details', model_budget_id=model_budget_id)


@login_required
def create_model_budget_expense(request, model_budget_id):
    '''view to create a new budget model expense'''
    form = forms.ModelExpenseForm(request.POST)
    if form.is_valid():
        model_expense_name = form.cleaned_data['model_expense_name']
        model_expense_amount = form.cleaned_data['model_expense_amount']
        response = budget_models.create_budget_model_expense(
            request=request, amount=model_expense_amount, name=model_expense_name, budget_id=model_budget_id)
        if response.status_code == status.HTTP_201_CREATED:
            messages.success(request, response.data['message'])
            return redirect('budget_model_details', model_budget_id=model_budget_id)
        messages.error(request, response.data['message'])
        return redirect('budget_model_details', model_budget_id=model_budget_id)
    messages.error(request, form.errors)
    return redirect('budget_model_details', model_budget_id=model_budget_id)


@login_required
def budget_model_details(request, model_budget_id):
    incomes = (budget_models.view_budget_model_incomes(request=request, budget_id=model_budget_id)).data['model_incomes']
    expenses = (budget_models.view_budget_model_expenses(request=request, budget_id=model_budget_id)).data['model_expenses']
    model_budget_name = get_object_or_404(
        models.BudgetModel, pk=model_budget_id)
    return render(request, 'budget-model-details.html', {'model_budget_id': model_budget_id, 'model_incomes': incomes, 'model_expenses': expenses, 'name': model_budget_name})

@login_required
def mark_budget_model_active(request, model_budget_id):
    response = budget_models.mark_budget_model_active(request=request, model_id=model_budget_id)
    messages.info(request, response.data['message'])
    return redirect('view_budget_models')


@login_required
def view_my_budgets(request):
    return render(request, 'budgets.html')


@login_required
def create_budget(request):
    form = forms.BudgetForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        response = budgets.create_budget(request=request, budget_name=name)
        if response.status_code == status.HTTP_201_CREATED:
            messages.success(request, response.data['message'])
            return redirect('my_budgets')
        else:
            messages.error(request, response.data['message'])
            return redirect('my_budgets')
    messages.error(request, form.errors)
    return redirect('my_budgets')
