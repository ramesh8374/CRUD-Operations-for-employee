from django import forms

class RegisterForm(forms.Form):
    firstname= forms.CharField(max_length=20, min_length=3)
    lastname= forms.CharField(max_length=20, min_length=3)
    email_id= forms.EmailField()
    phone_number= forms.IntegerField()
    age= forms.IntegerField()
    address= forms.CharField(max_length=256)
    password= forms.CharField(max_length=12, min_length=8)
    confirm_password= forms.CharField(max_length=12, min_length=8)