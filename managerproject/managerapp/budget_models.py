from django.core.exceptions import ObjectDoesNotExist
from rest_framework import response, status
from .models import BudgetModel, ModelIncome, ModelExpense


def create_budget(request, name):
    '''This method handles creation of a budget model'''
    try:
        BudgetModel.objects.get(budget_model_name=name)
        return response.Response({'message': 'A budget model with this nane already exists. Use a different name.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except ObjectDoesNotExist:
        new_budget_model = BudgetModel(
            budget_model_owner=request.user, budget_model_name=name)
        new_budget_model.save()
        return response.Response({'new_budget': new_budget_model}, status=status.HTTP_201_CREATED)


def view_model_budgets(request):
    '''This method gets all model budgets for a particular user'''
    budget_models = BudgetModel.objects.filter(budget_model_owner=request.user)
    return response.Response({'budget_models': budget_models}, status=status.HTTP_200_OK)


def create_budget_model_income(request, name, amount, model_budget_id):
    '''Create a model budget income'''
    try:
        ModelIncome.objects.get(model_income_name=name)
        return response.Response({'message': 'a model income with this name already exists. use a different name.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except ObjectDoesNotExist:
        new_budget_model_income = ModelIncome(
            model_income_name=name, model_income_amount=amount, budget_model_id=model_budget_id)
        new_budget_model_income.save()
        return response.Response({'new_model_income': new_budget_model_income, 'message': 'Income created succesfully!'}, status=status.HTTP_201_CREATED)