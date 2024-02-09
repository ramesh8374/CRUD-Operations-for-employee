from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
    emp_name = models.CharField(max_length=256)
    com_name = models.CharField(max_length=256)
    emp_email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    emp_address = models.CharField(max_length=256)
    emp_salary = models.IntegerField()

    def __str__(self):
        return self.emp_name