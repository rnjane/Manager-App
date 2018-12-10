from django.core.exceptions import ObjectDoesNotExist
from rest_framework import response
from . import models

def create_budget(request):
    #get the current budget model
    try:
        current_model_budget = models.BudgetModel.objects.get(current=True)
    except ObjectDoesNotExist:
        return response.Response({'message': 'no model budget yet'})



def create_a_new_budget(request):
    IncomeCategories.objects.all().delete()
    ExpenseCategories.objects.all().delete()

    #load new categories
    budget_model = BudgetModel.objects.get(budget_model_owner=request.user, current=True)
    budget_model_incomes = ModelIncome.objects.filter(budget_model_id=budget_model.id)
    budget_model_expenses = ModelExpense.objects.filter(budget_model_id=budget_model.id)
    for model_income in budget_model_incomes:
        new_income_category = IncomeCategories(name=model_income.model_income_name, amount=model_income.model_income_amount)
        new_income_category.save()
    for model_expense in budget_model_expenses:
        new_expense_category = ExpenseCategories(name=model_expense.model_expense_name, amount=model_expense.model_expense_amount)
        new_expense_category.save()