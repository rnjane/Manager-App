from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),

    # authentication urls
    path('login/', views.display_login_page, name='display-login'),
    path('perform-login/', views.perform_login, name='perform-login'),
    path('register/', views.display_register_page, name='display-register'),
    path('perform-register/', views.perform_register,
         name='perform_registration'),
    path('logout/', auth_views.logout, name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),

    # money budgeting urls
    path('budgets/', views.view_budget_models, name='view-money-dashboard'),
    path('budget-models/', views.view_budget_models, name='view_budget_models'),
    path('budget-model-details/', views.budget_model_details,
         name='budget_model_details'),
    path('create-budget-model/', views.create_budget_model,
         name='create_budget_model'),

    # time budgeting urls
    path('time/', views.view_time_dashboard, name='view-time-dashboard'),
    path('time-models/', views.view_time_models, name='view-time-models'),
]
