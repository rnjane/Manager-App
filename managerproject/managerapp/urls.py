from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.display_login_page, name='display-login'),
    path('perform-login/', views.perform_login, name='perform-login'),

    path('register/', views.display_register_page, name='display-register'),
    path('perform-register/', views.perform_register,
         name='perform_registration'),
]
