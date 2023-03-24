from django.shortcuts import render
from .models import Articles


def open(request):
    open = Articles.objects.all()
    return render(request,'open/open_home.html',{"open":open})
