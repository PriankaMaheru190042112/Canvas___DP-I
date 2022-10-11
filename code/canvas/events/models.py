from turtle import back
from unicodedata import name
from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.

class Event(models.Model):
    id= models.AutoField(primary_key= True)
    name = models.CharField( max_length=200)
    start_time= models.DateTimeField(blank=True, null=True)
    end_time= models.DateTimeField(blank=True, null=True)
    type= models.CharField(max_length=200)
    genre= models.CharField(max_length=200)
    photos_added= models.IntegerField(max_length=1, default=0)



    def __str__(self):
        return str(self.name)


    def get_absolute_url1(self):
        return reverse('events:event-detail', kwargs={'pk': self.pk})

    def get_absolute_url2(self):
        return reverse('organization:event_detail', kwargs={'pk': self.pk})    
        