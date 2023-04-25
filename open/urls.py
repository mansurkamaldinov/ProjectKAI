from django.urls import path
from . import views
urlpatterns = [
   path('',views.open,name = 'open_home'),
   path('crete/',views.crete,name="crete"),
   path('crete/creteras',views.creteras,name='creteras')






]
