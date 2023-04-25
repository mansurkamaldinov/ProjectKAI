from django.shortcuts import render
#from .models import Articles

def index(request):
    return render(request,'main/index.html')
def create(request):

    return render(request,'main/create.html')
def open(request):
    #opene = Articles.objects.all()
    return render(request,'open/open_home.html')#,{"open":opene})








