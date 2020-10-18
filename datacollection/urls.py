from django.contrib import admin
from django.urls import path
from datacollection.views import index
from datacollection.views import details

from datacollection import views


urlpatterns = [
    path("",views.index, name='home'),
    path("details/",views.details,name='details'),
    
    
]