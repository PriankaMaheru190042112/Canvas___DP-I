from django.contrib import admin
from .models import  Event, Image, User, Organization, Genre
# Register your models here.

admin.site.register(Event)
admin.site.register(Image)
admin.site.register(User)
admin.site.register(Organization)
admin.site.register(Genre)