from django.shortcuts import render,redirect
from .models import Articles,Employee
from .forms import ArticlesForm
from django.http import HttpResponse

def open(request):
    open = Articles.objects.all()
    return render(request,'open/open_home.html',{"open":open})
def crete(request):

    return render(request,'open/crete.html')


def creteras(request):
    error=''
    if request.method=="POST":
        form=ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('open_home')
        else:
            error='Not correct'


    form = ArticlesForm()
    data={
        "form":form

    }
    return render(request,'open/creteformras.html',data)


def create_employee(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        employee_name = request.POST.get('employee_name')
        company = Articles.objects.create(name=company_name)
        employee = Employee.objects.create(name=employee_name, company=company)
        return HttpResponse('Employee created successfully!')
    else:
        return render(request, 'create_employee.html')
