from django.contrib import admin
from .models import  Event, Image, Genre
# Register your models here.

admin.site.register(Event)
admin.site.register(Image)
admin.site.register(Genre)
