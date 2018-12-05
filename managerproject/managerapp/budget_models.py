from django.core.exceptions import ObjectDoesNotExist
from rest_framework import response, status
from .models import BudgetModel


def create_budget(request, name):
    '''This method handles creation of a budget model'''
    try:
        BudgetModel.objects.get(budget_model_name=name)
        return response.Response({'message': 'A budget model with this nane already exists. Use a different name.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except ObjectDoesNotExist:
        new_budget_model = BudgetModel(budget_model_owner=request.user, budget_model_name=name)
        new_budget_model.save()
        return response.Response({'new_budget': new_budget_model}, status=status.HTTP_201_CREATED)
