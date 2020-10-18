from django.shortcuts import render,HttpResponse
from datacollection.models import Datacollection
from datacollection.serializers import GetSerializer
# from datacollection import models
from datetime import date
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import generics
from rest_framework import mixins

from datacollection.models import Datacollection

d=date.today()

def index(request):
    
        
    
    return render(request,'index.html')

def details(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        date=request.POST.get('date')


        index=Datacollection(name=name,email=email,phone=phone,date=date)
        index.save()
        det=Datacollection.objects.all()
        return render(request,'details.html',{'stu':det})
    else:
        return render(request,'index.html')
