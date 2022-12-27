from django.contrib import admin
from .models import  Event, Images, Genre,Participant
# Register your models here.

admin.site.register(Event)
admin.site.register(Images)
admin.site.register(Genre)
admin.site.register(Participant)
