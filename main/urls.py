
from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name = 'home'),
 #  path('open',views.open,name='open'),
   path('create',views.create,name = 'create')



]
