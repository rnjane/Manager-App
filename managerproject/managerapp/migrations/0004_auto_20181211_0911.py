# Generated by Django 2.0.7 on 2018-12-11 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managerapp', '0003_expensecategories_incomecategories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetexpense',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='budgetincome',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
    ]
