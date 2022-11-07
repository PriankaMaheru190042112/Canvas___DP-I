from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    phone= models.CharField(max_length=200, null=True)
    profile_picture= models.CharField(max_length=200, null=True)
    isUser =  models.BooleanField(default=False, null=False)
    isOrganization =  models.BooleanField(default=False, null=False)
    isAdmin =  models.BooleanField(default=True, null=False)
    