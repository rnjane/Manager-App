from django.core.exceptions import ObjectDoesNotExist
from rest_framework import response, status
from django.shortcuts import get_list_or_404
from .models import TimeModel, ModelTimeSlot


def create_time_model(request, name):
    '''This method handles creation of a time model'''
    try:
        TimeModel.objects.get(time_model_name=name)
        return response.Response({'message': 'A time model with this nane already exists. Use a different name.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except ObjectDoesNotExist:
        new_time_model = TimeModel(
            time_model_owner=request.user, time_model_name=name)
        number_of_models = TimeModel.objects.filter(time_model_owner=request.user).count()
        if number_of_models == 0:
            new_time_model.current = True
        else:
            new_time_model.current = False
        new_time_model.save()
        return response.Response({'new_time_model': new_time_model}, status=status.HTTP_201_CREATED)


def view_model_times(request):
    '''This method gets all model times for a particular user'''
    time_models = TimeModel.objects.filter(time_model_owner=request.user)
    return response.Response({'time_models': time_models}, status=status.HTTP_200_OK)


# def create_a_model_time_slot(request, name, name, duration):
#     '''Create a model time income'''
#     try:
#         ModelIncome.objects.get(model_income_name=name, time_model_id=time_id)
#         return response.Response({'message': 'a model income with this name already exists. use a different name.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
#     except ObjectDoesNotExist:
#         new_time_model_income = ModelIncome(
#             model_income_name=name, model_income_amount=amount, time_model_id=time_id)
#         new_time_model_income.save()
#         return response.Response({'new_model_income': new_time_model_income, 'message': 'Income created succesfully!'}, status=status.HTTP_201_CREATED)


# def view_time_model_incomes(request, time_id):
#     '''view all incomes in a certain time model'''
#     try:
#         model_incomes = ModelIncome.objects.filter(time_model_id=time_id)
#         return response.Response({'model_incomes': model_incomes}, status=status.HTTP_200_OK)
#     except ObjectDoesNotExist:
#         return response.Response({'model_incomes': []}, status=status.HTTP_404_NOT_FOUND)


# def mark_time_model_active(request, model_id):
#     current_model_time = TimeModel.objects.filter(time_model_owner_id=request.user, id=model_id)
#     if current_model_time.exists():
#         #clear the current categories
#         IncomeCategories.objects.all().delete()
#         ExpenseCategories.objects.all().delete()

#         #load new categories
#         time_model_incomes = ModelIncome.objects.filter(time_model_id=model_id)
#         time_model_expenses = ModelExpense.objects.filter(time_model_id=model_id)
#         for model_income in time_model_incomes:
#             new_income_category = IncomeCategories(name=model_income.model_income_name, amount=model_income.model_income_amount, owner=request.user)
#             new_income_category.save()
#         for model_expense in time_model_expenses:
#             new_expense_category = ExpenseCategories(name=model_expense.model_expense_name, amount=model_expense.model_expense_amount, owner=request.user)
#             new_expense_category.save()
#         old_current_model_time = TimeModel.objects.filter(time_model_owner_id=request.user, current=True)
#         old_current_model_time.update(current=False)
#         current_model_time.update(current=True)
#         return response.Response({'message': 'Model time marked active succesfully'}, status=status.HTTP_200_OK)
#     else:
#         return response.Response({'message': 'There is no time model with the given model id'}, status=status.HTTP_404_NOT_FOUND)
