from django.core.exceptions import ObjectDoesNotExist
from rest_framework import response, status
from . import models

def create_budget(request, budget_name):
    models.Budget
    try:
        models.Budget.objects.get(owner=request.user, name=budget_name)
        return response.Response({'message': 'This name is already in use'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except ObjectDoesNotExist:
        new_budget = models.Budget(owner=request.user, name=budget_name)
        new_budget.save()
        return response.Response({'message': 'budget created succesfully'}, status=status.HTTP_201_CREATED)

# def create_a_new_budget(request):
#     #load new categories
#     budget_model = BudgetModel.objects.get(budget_model_owner=request.user, current=True)
#     budget_model_incomes = ModelIncome.objects.filter(budget_model_id=budget_model.id)
#     budget_model_expenses = ModelExpense.objects.filter(budget_model_id=budget_model.id)
#     for model_income in budget_model_incomes:
#         new_income_category = IncomeCategories(name=model_income.model_income_name, amount=model_income.model_income_amount)
#         new_income_category.save()
#     for model_expense in budget_model_expenses:
#         new_expense_category = ExpenseCategories(name=model_expense.model_expense_name, amount=model_expense.model_expense_amount)
#         new_expense_category.save()