from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from rest_framework import response, status
from . import models

def create_budget(request, budget_name):
    try:
        models.Budget.objects.get(owner=request.user, name=budget_name)
        return response.Response({'message': 'This name is already in use'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except ObjectDoesNotExist:
        new_budget = models.Budget(owner=request.user, name=budget_name)
        new_budget.save()
        return response.Response({'message': 'budget created succesfully'}, status=status.HTTP_201_CREATED)

def view_all_budgets(request):
    try:
        budgets = models.Budget.objects.filter(owner=request.user)
        for budget in budgets:
            total_income = models.BudgetIncome.objects.filter(budget_id=budget.id).aggregate(Sum('amount'))['amount__sum']
            total_expenses = models.BudgetExpense.objects.filter(budget_id=budget.id).aggregate(Sum('amount'))['amount__sum']
            if total_income is None:
                budget.total_income = 0.00
            else:
                budget.total_income = total_income
            if total_expenses is None:
                budget.total_expenses = 0.00
            else:
                budget.total_expenses = total_expenses
        return response.Response({'budgets': budgets}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return response.Response({'budgets': []})

def create_income(request, budget_id, income_name, income_amount, category, description):
    income = models.BudgetIncome(budget_id = budget_id, name = income_name, amount = income_amount, category=category, description=description)
    income.save()
    incomes = models.BudgetIncome.objects.filter(budget_id=budget_id)
    return(incomes)

def view_all_incomes(request, budget_id):
    incomes = models.BudgetIncome.objects.filter(budget_id = budget_id)
    return(incomes)

def edit_income(request, budget_id, income_id, income_new_name, income_new_amount):
    income = models.BudgetIncome.objects.filter(pk=income_id)
    income.update(name=income_new_name, amount=income_new_amount)
    incomes = models.BudgetIncome.objects.filter(budget_id = budget_id)
    return(incomes)

def delete_income(request, budget_id, income_id):
    income = models.BudgetIncome.objects.filter(pk=income_id)
    income.delete()
    incomes = models.BudgetIncome.objects.filter(budget_id = budget_id)
    return(incomes)

def view_all_expenses(request, budget_id):
    expenses = models.BudgetExpense.objects.filter(budget_id = budget_id)
    return(expenses)

def create_expense(request, budget_id, expense_name, expense_amount):
    expense = models.BudgetExpense(budget_id = budget_id, name = expense_name, amount = expense_amount)
    expense.save()
    expenses = models.BudgetExpense.objects.filter(budget_id = budget_id)
    return(expenses)

def edit_expense(request, budget_id, expense_id, expense_new_name, expense_new_amount):
    expense = models.BudgetExpense.objects.filter(pk = expense_id)
    expense.update(name=expense_new_name, amount=expense_new_amount)
    expenses = models.BudgetExpense.objects.filter(budget_id = budget_id)
    return(expenses)

def delete_expense(request, budget_id, expense_id):
    expense = models.BudgetExpense.objects.filter(pk=expense_id)
    expense.delete()
    expenses = models.BudgetExpense.objects.filter(budget_id = budget_id)
    return(expenses)

def get_all_income_categories(request):
    try:
        my_categories = models.IncomeCategories.objects.filter(owner=request.user)
        return response.Response({'income_categories': my_categories}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return response.Response({'income_categoris': []})

def get_all_expense_categories(request):
    try:
        my_categories = models.ExpenseCategories.objects.filter(owner=request.user)
        return response.Response({'expense_categories': my_categories}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return response.Response({'expense_categories': []})