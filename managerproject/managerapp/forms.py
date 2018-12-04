from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=50)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(max_length=100)