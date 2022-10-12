from distutils.command.upload import upload
from email.policy import default
from turtle import back
from unicodedata import name
from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.

class Event(models.Model):
    id= models.IntegerField(primary_key= True)
    name = models.CharField( max_length=200)
    start_time= models.DateTimeField(blank=True, null=True)
    end_time= models.DateTimeField(blank=True, null=True)
    type= models.CharField(max_length=200)
    genre= models.CharField(max_length=200)
    fee= models.IntegerField(max_length=200, default=0)
    photos_added= models.IntegerField(max_length=1, default=0)
    # organization= models.ForeignKey(Organization, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id)


    def get_absolute_url1(self):
        return reverse('events:event-detail', kwargs={'pk': self.pk})

    def get_absolute_url2(self):
        return reverse('organization:event_detail', kwargs={'pk': self.pk})    
        

class Image(models.Model):
    event_id= models.ForeignKey(Event, on_delete=models.CASCADE)
    path = models.ImageField(upload_to = 'images', default="")
    artist_name= models.CharField(max_length=200)
    size= models.IntegerField(max_length=200)
    price= models.IntegerField(max_length=200)
    

    def __str__(self):
        return str(self.event_id)



class User(models.Model):
    id= models.IntegerField(primary_key= True)
    name = models.CharField( max_length=200)
    email= models.EmailField(max_length=200)
    password= models.CharField(max_length=200)
    phone= models.IntegerField(max_length=200)
    profile_picture= models.CharField(max_length=200)
    

    def __str__(self):
        return str(self.name)


class Organization(models.Model):
    id= models.IntegerField(primary_key= True)
    name = models.CharField( max_length=200)
    email= models.EmailField(max_length=200)
    password= models.CharField(max_length=200)
    phone= models.IntegerField(max_length=200)
    profile_picture= models.CharField(max_length=200)
    


    def __str__(self):
        return str(self.id)    