# Generated by Django 2.0.7 on 2018-12-20 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managerapp', '0008_auto_20181220_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modeltimeslot',
            old_name='model_slot_name',
            new_name='model_time_slot_name',
        ),
    ]
