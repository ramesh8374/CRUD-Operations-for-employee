from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):

    return render(request, 'App\Home.html')

def Login(request):

    return render(request,'App\Login.html')



