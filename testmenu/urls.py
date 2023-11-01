from django.urls import path
from . import views

urlpatterns = [
    path('', views.showhomepage, name='home'),
   
]