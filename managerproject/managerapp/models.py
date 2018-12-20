from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class BudgetModel(models.Model):
    budget_model_owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    budget_model_name = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    current = models.BooleanField(default=False)

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


class Budget(models.Model):
    owner = models.ForeignKey(User, related_name='budget', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    incomes = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    expenses = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_created']


class BudgetIncome(models.Model):
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    category = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    budget = models.ForeignKey(Budget, related_name='budgetincome', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_created']


class BudgetExpense(models.Model):
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    category = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    budget = models.ForeignKey(Budget, related_name='budgetexpense', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_created']

class IncomeCategories(models.Model):
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    owner = models.ForeignKey(User, related_name='income_categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ExpenseCategories(models.Model):
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    owner = models.ForeignKey(User, related_name='expense_categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TimeModel(models.Model):
    time_model_owner = models.ForeignKey(User, related_name='time_model_owner', on_delete=models.CASCADE)
    time_model_name = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    current = models.BooleanField(default=False)

    def __repr__(self):
        return self.time_model_name

    class Meta:
        ordering = ['date_created']


class ModelTimeSlot(models.Model):
    time_model = models.ForeignKey(TimeModel, related_name='time_model', on_delete=models.CASCADE)
    model_slot_name = models.CharField(max_length=30)
    model_slot_duration = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return self.model_slot_name

    class Meta:
        ordering = ['date_created']
