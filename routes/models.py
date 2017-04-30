from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Areas(models.Model):
    areas_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.areas_text
        
class Routes(models.Model):
    Areas = models.ForeignKey(Areas, on_delete=models.CASCADE)
    routes_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.routes_text