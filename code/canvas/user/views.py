from django.shortcuts import render
from .models import Event,Image,User,Organization
from django.views.generic import ListView, DetailView
# Create your views here.


def user_auth(request):
    # return HttpResponse("Starting the project")
    return render(request, 'user/user_auth.html') 


def user_home(request):
    # return HttpResponse("Starting the project")
   objects = Event.objects.all()
   return render(request, 'user/user_home.html',{'objects':objects}) 

def user_profile(request):
    # return HttpResponse("Starting the project")
    return render(request, 'user/user_profile.html') 


def user_gallery(request):
    # return HttpResponse("Starting the project")
    return render(request, 'user/user_gallery.html') 

class EventDetail(DetailView):
    model= Event
    template_name= 'user/event_details.html'    