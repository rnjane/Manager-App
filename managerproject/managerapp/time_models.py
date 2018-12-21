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

def create_time_slot(request, name, hours, minutes, weekday, time_id):
    '''This method handles creation of a time model'''
    try:
        ModelTimeSlot.objects.get(model_time_slot_name=name)
        return response.Response({'message': 'A time slot with this nane already exists. Use a different name.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except ObjectDoesNotExist:
        duration = hours + (minutes/60)
        rounded_duration = round(duration, 4)
        if weekday == 'WeekDay':
            wkday = True
        else:
            wkday = False
        new_time_model = ModelTimeSlot(
            model_time_slot_name=name, model_slot_duration=rounded_duration, weekday=wkday, time_model_id=time_id)
        new_time_model.save()
        return response.Response({'new_time_model': new_time_model, 'message': 'Time slot created succesfully!'}, status=status.HTTP_201_CREATED)

def view_time_slots(request, time_id):
    '''view all time slots in a time model'''
    try:
        time_slots = ModelTimeSlot.objects.filter(time_model_id=time_id)
        return response.Response({'time_slots': time_slots}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return response.Response({'time_slots': []}, status=status.HTTP_404_NOT_FOUND)

def view_budget_model_incomes(request, budget_id):
    '''view all incomes in a certain budget model'''
    try:
        model_incomes = ModelIncome.objects.filter(budget_model_id=budget_id)
        return response.Response({'model_incomes': model_incomes}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return response.Response({'model_incomes': []}, status=status.HTTP_404_NOT_FOUND)
