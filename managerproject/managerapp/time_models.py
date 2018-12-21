from django.core.exceptions import ObjectDoesNotExist
from rest_framework import response, status
from django.shortcuts import get_list_or_404
import datetime
from .models import TimeModel, ModelTimeSlot, CurrentTimeSlot, ScheduledDay


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

def mark_time_model_active(request, model_id):
    current_model_time = TimeModel.objects.filter(time_model_owner_id=request.user, id=model_id)
    if current_model_time.exists():
        #clear the current categories
        CurrentTimeSlot.objects.all().delete()

        #get time slots from the model time that is to be made active
        model_time_slots = ModelTimeSlot.objects.filter(time_model_id=model_id)

        #populate current time slots
        for model_time_slot in model_time_slots:
            new_time_slot = CurrentTimeSlot(name=model_time_slot.model_time_slot_name, duration=model_time_slot.model_slot_duration, weekday=model_time_slot.weekday, owner=request.user)
            new_time_slot.save()
        
        #mark the previous model time inactive
        old_current_time_model = TimeModel.objects.filter(time_model_owner_id=request.user, current=True)
        old_current_time_model.update(current=False)

        #mark the current model time active
        current_model_time.update(current=True)
        return response.Response({'message': 'Model time marked active succesfully'}, status=status.HTTP_200_OK)
    else:
        return response.Response({'message': 'There is no time model with the given model id'}, status=status.HTTP_404_NOT_FOUND)

def create_a_scheduled_day(request, name):
    try:
        ScheduledDay.objects.get(name=name)
        return response.Response({'message': 'This name is already in use. Use a different one.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except ObjectDoesNotExist:
        new_scheduled_day = ScheduledDay(name=name, owner=request.user)
        new_scheduled_day.save()
        return response.Response({'message': 'Scheduled day created succesfully'}, status=status.HTTP_201_CREATED)

def view_schedled_days(request):
    try:
        days = ScheduledDay.objects.filter(owner=request.user)
        return response.Response({'days': days}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return response.Response({'days': []}, status=status.HTTP_404_NOT_FOUND)