from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import EmployeeDetails, RegisterDetails
from .forms import RegisterForm

# Create your views here.
def worldcup(request):
    date=datetime.datetime.now().date()
    time=datetime.datetime.now().time()
    dic={'date':date, 'time':time,'name':'ALAPAKU RAMESH'}
    return render(request,'SecondApp\worldcuptable.html', context=dic)

def product(request):
    return render(request,"App/product.html")

def product_total(request):
    mob = int(request.GET['mobile'])
    lap = int(request.GET['laptop'])
    desk = int(request.GET['desktop'])
    key = int(request.GET['keyboard'])
    mou = int(request.GET['mouse'])
    total = mob+lap+desk+key+mou

    return render(request,'SecondApp/pro_details.html',context={"total":total})


def emp_details(request):
    emp = EmployeeDetails.objects.all()
    return render(request, "SecondApp/emp_details.html",context={"emp":emp})

def register(request):
    form = RegisterForm()
    return render(request,"SecondApp/register.html", context={'form':form})


def registerdetails(request):
    if request.method=='POST':
        if (request.POST.get("firstname") and request.POST.get("lastname") and request.POST.get("email_id") and request.POST.get("phone_number") and request.POST.get("age") and request.POST.get("address") and request.POST.get("password") and request.POST.get("confirm_password")):

            reg = RegisterDetails()
            reg.firstname = request.POST.get("firstname")
            reg.lastname = request.POST.get("lastname")
            reg.email_id = request.POST.get("email_id")
            reg.phone_number = request.POST.get("phone_number")
            reg.age = request.POST.get("age")
            reg.address = request.POST.get("address")
            reg.password = request.POST.get("password")
            reg.confirm_password = request.POST.get("confirm_password")
            reg.save()

    form = RegisterForm()
    return render(request, "SecondApp/register.html", context={'form': form})