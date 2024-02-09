from django.shortcuts import render, HttpResponse,redirect, get_object_or_404
from .models import EmployeeDetails
from .forms import EmployeeForm
#from django.core import serializers

# Create your views here.

def employeedetails(request):
    emp = EmployeeDetails.objects.all()

    #for JSON Format:
    #data = serializers.serialize("json",emp)
    #return HttpResponse(data, content_type='application/json')
    return render(request,'CURDApp/employee.html', context={'emp':emp})

def addemployee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("""<h1>Employee is added Successfully
                                <h2><a href="/CURDApp/employeedetails/">Click Here</a>View Employee Table</h2>
                                </h1>""")
    return render(request,'CURDApp/addemployee.html', context={'form': form})


def delete(request,id):
    emp = EmployeeDetails.objects.get(id=id)
    emp.delete()
    return redirect("/CURDApp/employeedetails/")


def update(request,id):
    instance = get_object_or_404(EmployeeDetails, id=id)
    form = EmployeeForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        form = EmployeeForm(instance=instance, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("""<h1>Employee is added Successfully
                                            <h2><a href="/CURDApp/employeedetails/">Click Here</a>View Employee Table</h2>
                                            </h1>""")
    return render(request,'CURDApp/updateemployee.html', context={'form':form})


