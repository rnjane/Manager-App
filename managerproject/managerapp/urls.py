from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # authentication urls
    path('login/', views.display_login_page, name='display-login'),
    path('perform-login/', auth_views.login, {'template_name': 'core/login.html'}, name='perform-login'),
    path('register/', views.display_register_page, name='display-register'),
    path('perform-register/', views.perform_register,
         name='perform_registration'),
    path('logout/', auth_views.logout, name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),

    #budget urls
    path('budgets/', views.view_my_budgets, name='my_budgets'),
    path('create-budget/', views.create_budget, name='create_budget'),
    path('delete-budget/<int:budget_id>/', views.delete_budget, name='delete_budget'),

    # money-budget models urls
    path('budget-models/', views.view_budget_models, name='view_budget_models'),
    path('budget-model-details/<int:model_budget_id>/', views.budget_model_details,
         name='budget_model_details'),
    path('create-budget-model/', views.create_budget_model,
         name='create_budget_model'),
    path('mark-budget-model-active/<int:model_budget_id>', views.mark_budget_model_active, name='mark_budget_model_active'),
    path('delete-model-budget/<int:model_budget_id>', views.delete_budget_model, name='delete_model_budget'),

    # budget model expenses urls
    path('create-model-budget-expense/<int:model_budget_id>/',
         views.create_model_budget_expense, name='create_model_budget_expense'),

    # budget model incomes urls
    path('create-model-budget-income/<int:model_budget_id>/',
         views.create_model_budget_income, name='create_model_budget_income'),

    # time budgeting urls
    path('time/', views.view_time_dashboard, name='view-time-dashboard'),
    path('time-models/', views.view_time_models, name='view-time-models'),

    #budget incomes
    path('<int:budget_id>/create-budget-income/', views.create_income, name='create_income'),
    path('<int:budget_id>/incomes/', views.view_all_incomes, name='view_incomes'),
    path('<int:budget_id>/income/<int:income_id>/edit-income/', views.edit_income, name='edit_income'),
    path('<int:budget_id>/dincome/<int:income_id>/delete-income/', views.delete_income, name='delete_income'),

    #budget expenses
    path('<int:budget_id>/create-budget-expense/', views.create_expense, name='create_expense'),
    path('<int:budget_id>/expenses/', views.view_all_expenses, name='view_expenses'),
    path('<int:budget_id>/budget/<int:expense_id>/edit-expense/', views.edit_expense, name='edit_expense'),
    path('<int:budget_id>/budget/<int:expense_id>/delete-expense/', views.delete_expense, name='delete_expense'),

    # time budget models urls
    path('time-models/', views.view_time_models, name='view_time_models'),
    path('create-time-model/', views.create_time_model,
         name='create_time_model'),
     path('time-model-details/<int:model_time_id>/', views.time_model_details,
         name='time_model_details'),
     path('create-time-slot/<int:model_time_id>/', views.create_time_slot, name='create_time_slot'),
     path('mark-time-model-active/<int:model_time_id>/', views.mark_time_model_active, name='mark_time_model_active'),
     path('delete-time-budget/<int:model_time_id>', views.delete_budget_model, name='delete_time_budget'),

     #scheduled day
     # path('create-scheduled-day', views)
]
