from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import status
from . import forms, user_auth


def index(request):
    return render(request, 'register.html')


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
            return redirect('display-register')
        else:
            messages.error(request, response.data['message'])
            return redirect('display-login')
    else:
        messages.error(request, form.errors)
        return redirect('display-login')
