from django.db import models
from datetime import  date

# Create your models here.
class Datacollection(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    date=models.DateField()
    
    
    
    
