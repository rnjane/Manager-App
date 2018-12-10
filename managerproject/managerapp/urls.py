from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # authentication urls
    path('login/', views.display_login_page, name='display-login'),
    path('perform-login/', views.perform_login, name='perform-login'),
    path('register/', views.display_register_page, name='display-register'),
    path('perform-register/', views.perform_register,
         name='perform_registration'),
    path('logout/', auth_views.logout, name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),

    #budget urls
    path('budgets/', views.view_my_budgets, name='my_budgets'),
    path('create-budget/', views.create_budget, name='create_budget'),

    # money-budget models urls
    path('budget-models/', views.view_budget_models, name='view_budget_models'),
    path('budget-model-details/<int:model_budget_id>/', views.budget_model_details,
         name='budget_model_details'),
    path('create-budget-model/', views.create_budget_model,
         name='create_budget_model'),
    path('mark-budget-model-active/<int:model_budget_id>', views.mark_budget_model_active, name='mark_budget_model_active'),

    # budget model expenses urls
    path('create-model-budget-expense/<int:model_budget_id>/',
         views.create_model_budget_expense, name='create_model_budget_expense'),

    # budget model incomes urls
    path('create-model-budget-income/<int:model_budget_id>/',
         views.create_model_budget_income, name='create_model_budget_income'),

    # time budgeting urls
    path('time/', views.view_time_dashboard, name='view-time-dashboard'),
    path('time-models/', views.view_time_models, name='view-time-models'),
]
