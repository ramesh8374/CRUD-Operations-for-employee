import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","PythonProject1.settings")

import django

django.setup()

from CURDApp.models import EmployeeDetails
from faker import Faker
from random import *

faker = Faker()
def fakeemployeedatas():
    f_empid = randint(200, 999)
    f_name = faker.name()
    f_com = faker.name()
    f_email = faker.email()
    f_phone = randint(7000000000, 9000000000)
    f_address = faker.city()
    f_salary = randint(20000, 70000)
    emp = EmployeeDetails.objects.get_or_create(emp_name = f_name,
                                                emp_id = f_empid,
                                                com_name = f_com,
                                                emp_email = f_email,
                                                phone_number = f_phone,
                                                emp_address = f_address,
                                                emp_salary = f_salary
                                                )
for i in range(0,10):
    fakeemployeedatas()

