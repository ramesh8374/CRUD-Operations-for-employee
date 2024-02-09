from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
    emp_name = models.CharField(max_length=256)
    emp_id = models.CharField(max_length=256)
    com_name = models.CharField(max_length=256)
    emp_email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    emp_address = models.CharField(max_length=256)
    emp_salary = models.IntegerField()


    def __str__(self):
        return self.emp_name



class RegisterDetails(models.Model):
    firstname= models.CharField(max_length=20)
    lastname= models.CharField(max_length=20)
    email_id= models.EmailField()
    phone_number= models.IntegerField()
    age= models.IntegerField()
    address= models.CharField(max_length=256)
    password= models.CharField(max_length=12)
    confirm_password= models.CharField(max_length=12)

    def __str__(self):
        return self.firstname