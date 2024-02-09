from .models import EmployeeDetails
from django import forms

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetails
        fields = "__all__"