from django.shortcuts import render
from .models import UserTable

# Create your views here.
def User(request):
    return render(request,'ThirdApp/home.html')

def user_details(request):
    emp = UserTable.objects.all()
    return render(request,'ThirdApp/user_details.html',context={'emp':emp})