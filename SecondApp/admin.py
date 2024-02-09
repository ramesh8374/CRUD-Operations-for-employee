from django.contrib import admin
from .models import EmployeeDetails, RegisterDetails

# Register your models here.
admin.site.register(EmployeeDetails)
admin.site.register(RegisterDetails)