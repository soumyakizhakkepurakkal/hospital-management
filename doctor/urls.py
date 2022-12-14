from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('departments',views.department,name='departement'),
    path('doctor',views.doctor,name='doctor'),
    path('booking',views.booking,name='booking'),
]