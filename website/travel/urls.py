from django.urls import path
from . import views

urlpatterns = [
    path('banglore', views.banglore, name = 'banglore'),
    path('chennai', views.chennai, name = 'chennai'),
    path('mumbai', views.mumbai, name = 'mumbai'),
    path('pune', views.pune, name = 'pune'),
    path('hyderabad', views.hyderabad, name = 'hyderabad'),
    path('', views.index, name = 'index')
#    path('addmul', views.addmul, name= 'addmul')
]