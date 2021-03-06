from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models


# Create your models here.

class Area(models.Model):
    areas_text = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=1000, null=True)
    #pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.areas_text
        
class Route(models.Model):
    Area = models.ForeignKey(Area, on_delete=models.CASCADE)
    routes_text = models.CharField(max_length=200)
    rating = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=500, null=True)
    comments = models.CharField(max_length=1000, null=True)
    #picture_text = models.CharField(max_length=500, null=True)
    
    def __str__(self):
        return self.routes_text
        