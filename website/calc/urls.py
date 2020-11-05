from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name = 'home'),
    path('addmul', views.addmul, name= 'addmul')
]