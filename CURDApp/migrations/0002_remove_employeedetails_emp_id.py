# Generated by Django 4.2.7 on 2023-11-22 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CURDApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeedetails',
            name='emp_id',
        ),
    ]
