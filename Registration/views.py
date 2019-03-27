from django.shortcuts import render,redirect
from .models import Employee
# Create your views here.
from .forms import EmployeeForm

def show_details(request):
    employees=Employee.objects.all()
    form=EmployeeForm()
    return render(request,"index.html",{"employees":employees,"form":form})


def Add_empDetails(request):
    if request.method =='POST':
        form=EmployeeForm(request.POST)
        print("hiii")
        form.save()
    return redirect('/show')


def delete_Emp(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")

