from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class BudgetModel(models.Model):
    budget_model_owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    budget_model_name = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.budget_model_name

    class Meta:
        ordering = ['date_created']


class ModelIncome(models.Model):
    model_income_name = models.CharField(max_length=30)
    model_income_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    budget_model = models.ForeignKey(BudgetModel, related_name='model_income', on_delete=models.CASCADE)

    def __str__(self):
        return self.model_income_name

    class Meta:
        ordering = ['model_income_amount']


class ModelExpense(models.Model):
    model_expense_name = models.CharField(max_length=30)
    model_expense_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    budget_model = models.ForeignKey(BudgetModel, related_name='model_expense', on_delete=models.CASCADE)

    def __str__(self):
        return self.model_expense_name

    class Meta:
        ordering = ['model_expense_amount']

