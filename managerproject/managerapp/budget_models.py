from django.core.exceptions import ObjectDoesNotExist
from rest_framework import response, status
from django.shortcuts import get_list_or_404
from .models import BudgetModel, ModelIncome, ModelExpense, IncomeCategories, ExpenseCategories


def create_budget(request, name):
    '''This method handles creation of a budget model'''
    try:
        BudgetModel.objects.get(budget_model_name=name)
        return response.Response({'message': 'A budget model with this nane already exists. Use a different name.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except ObjectDoesNotExist:
        new_budget_model = BudgetModel(
            budget_model_owner=request.user, budget_model_name=name)
        number_of_models = BudgetModel.objects.filter(budget_model_owner=request.user).count()
        if number_of_models == 0:
            new_budget_model.current = True
        else:
            new_budget_model.current = False
        new_budget_model.save()
        return response.Response({'new_budget': new_budget_model}, status=status.HTTP_201_CREATED)


def view_model_budgets(request):
    '''This method gets all model budgets for a particular user'''
    budget_models = BudgetModel.objects.filter(budget_model_owner=request.user)
    return response.Response({'budget_models': budget_models}, status=status.HTTP_200_OK)


def create_budget_model_income(request, name, amount, budget_id):
    '''Create a model budget income'''
    try:
        ModelIncome.objects.get(model_income_name=name, budget_model_id=budget_id)
        return response.Response({'message': 'a model income with this name already exists. use a different name.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except ObjectDoesNotExist:
        new_budget_model_income = ModelIncome(
            model_income_name=name, model_income_amount=amount, budget_model_id=budget_id)
        new_budget_model_income.save()
        return response.Response({'new_model_income': new_budget_model_income, 'message': 'Income created succesfully!'}, status=status.HTTP_201_CREATED)


def create_budget_model_expense(request, name, amount, budget_id):
    '''create a model budget expense'''
    try:
        ModelExpense.objects.get(
            model_expense_name=name, budget_model_id=budget_id)
        return response.Response({'message': 'a model expense with this name already exists. please use a different name.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except ObjectDoesNotExist:
        new_budget_model_expense = ModelExpense(
            model_expense_name=name, model_expense_amount=amount, budget_model_id=budget_id)
        new_budget_model_expense.save()
        return response.Response({'new_model_budget_expense': new_budget_model_expense, 'message': 'Expense created succesfully!'}, status=status.HTTP_201_CREATED)

def view_budget_model_incomes(request, budget_id):
    '''view all incomes in a certain budget model'''
    try:
        model_incomes = ModelIncome.objects.filter(budget_model_id=budget_id)
        return response.Response({'model_incomes': model_incomes}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return response.Response({'model_incomes': []}, status=status.HTTP_404_NOT_FOUND)

def view_budget_model_expenses(request, budget_id):
    '''view all expenses in a certain budget model'''
    try:
        model_expenses = ModelExpense.objects.filter(budget_model_id=budget_id)
        return response.Response({'model_expenses': model_expenses}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return response.Response({'model_expenses': []}, status=status.HTTP_404_NOT_FOUND)

def mark_budget_model_active(request, model_id):
    current_model_budget = BudgetModel.objects.filter(budget_model_owner_id=request.user, id=model_id)
    if current_model_budget.exists():
        #clear the current categories
        IncomeCategories.objects.all().delete()
        ExpenseCategories.objects.all().delete()

        #load new categories
        budget_model_incomes = ModelIncome.objects.filter(budget_model_id=model_id)
        budget_model_expenses = ModelExpense.objects.filter(budget_model_id=model_id)
        for model_income in budget_model_incomes:
            new_income_category = IncomeCategories(name=model_income.model_income_name, amount=model_income.model_income_amount, owner=request.user)
            new_income_category.save()
        for model_expense in budget_model_expenses:
            new_expense_category = ExpenseCategories(name=model_expense.model_expense_name, amount=model_expense.model_expense_amount, owner=request.user)
            new_expense_category.save()
        old_current_model_budget = BudgetModel.objects.filter(budget_model_owner_id=request.user, current=True)
        old_current_model_budget.update(current=False)
        current_model_budget.update(current=True)
        return response.Response({'message': 'Model budget marked active succesfully'}, status=status.HTTP_200_OK)
    else:
        return response.Response({'message': 'There is no budget model with the given model id'}, status=status.HTTP_404_NOT_FOUND)
