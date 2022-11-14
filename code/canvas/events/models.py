from distutils.command.upload import upload
from email.policy import default
from enum import unique
from turtle import back
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
from datetime import datetime
from cryptography.fernet import Fernet
from django.contrib.auth.models import AbstractUser
import os
from django.template.defaultfilters import slugify
from authentication_user.models import User
# Create your models here.

class Event(models.Model):
    id= models.IntegerField(primary_key=True)
    name = models.CharField( max_length=200)
    description = models.CharField( max_length=200)
    start_date= models.DateField(blank=True, null=True)
    start_time= models.TimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    end_date= models.DateTimeField(null= True, blank=True)
    end_time= models.TimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    genre= models.CharField(max_length=200)
    fee= models.IntegerField(max_length=200, default=0, null=True)
    # organization= models.ForeignKey(Organization, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.name)
    

    def get_absolute_url1(self):
        return reverse('events:event-detail', kwargs={'pk': self.pk})

    def get_absolute_url2(self):
        return reverse('organization:event_detail', kwargs={'pk': self.pk}) 
    def get_absolute_url3(self):
        return reverse('user:event_detail', kwargs={'pk': self.pk})        
    
def get_image_filename(instance, filename):
        name = instance.event.name
        slug = slugify(name)
        return "images/%s-%s" % (slug, filename)  
   

class Image(models.Model):
    event_id= models.ForeignKey(Event, on_delete=models.CASCADE)
    image= models.ImageField(upload_to=get_image_filename, verbose_name='Image')
    # img_path = models.ImageField(upload_to = 'event_images')
    img_price =models.IntegerField(max_length = 100, default=0, null= True)
    frame_height = models.IntegerField(max_length=200)
    frame_width = models.IntegerField(max_length= 200)
    # path = models.ImageField(upload_to = 'images', default="")
    # artist_name= models.CharField(max_length=200)
    # size= models.IntegerField(max_length=200)
    # price= models.IntegerField(max_length=200)
    

    # def __str__(self):
    #     return str(self.event_id)


class Genre(models.Model):
    genre_id =models.IntegerField(primary_key= True)
    genre_name= models.CharField(max_length=200)






#     def __str__(self):
#         return str(self.name)
    
        


# class Organization(models.Model):
#     id= models.IntegerField(primary_key= True)
#     name = models.CharField( max_length=200, default="")
#     email= models.EmailField(max_length=200, unique=True)
#     password= models.CharField(max_length=200)
#     phone= models.IntegerField(max_length=200, null=True)
#     profile_picture= models.CharField(max_length=200, null=True)
#     USERNAME_FIELD= ['email']
#     REQUIRED_FIELDS = ['name']


#     def __str__(self):
#         return str(self.id)    

    