from importlib.resources import path
from tkinter.messagebox import NO
from django.shortcuts import render
from django.http import HttpResponse

from events.models import Image
from .models import Event,Image,User,Organization
from django.views.generic import ListView, DetailView


# Create your views here.

def eventform(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        start_time = request.POST.get('start_time',None)
        end_time = request.POST.get('end_time', None)
        type = request.POST.get('type', '')
        genre = request.POST.get('genre', '')
        images= request.FILES.get('images')
        event= Event(name= name, start_time=start_time, end_time=end_time, type=type, genre=genre)

        image= Image.objects.create(
            path= images,
        )
       
        event.save()
        image.save()
    return render(request, 'organization/eventform.html')


def organization_auth(request):
    # return HttpResponse("Starting the project")
    return render(request, 'organization/organization_auth.html') 


def organization_home(request):
    # return HttpResponse("Starting the project")
    return render(request, 'organization/organization_home.html') 
    
    
def organization_profile(request):
    # return HttpResponse("Starting the project")
    return render(request, 'organization/organization_profile.html') 


class EventsView(ListView):
    model= Event
    template_name = 'organization/events.html'

class EventDetail(DetailView):
    model= Event
    template_name= 'organization/eventDetail.html'