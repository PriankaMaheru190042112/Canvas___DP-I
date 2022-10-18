from django.shortcuts import render
from events.models import User,Organization, Event,Image
from django.views.generic import ListView, DetailView
# Create your views here.
from django.utils.timezone import now

def user_auth(request):
    # return HttpResponse("Starting the project")
    return render(request, 'user/user_auth.html') 


def user_home(request):
    # return HttpResponse("Starting the project")
   objects = Event.objects.all()
   today = now().date()
   objects= Event.objects.filter(start_date__gte=today).order_by('start_date')[:3]
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