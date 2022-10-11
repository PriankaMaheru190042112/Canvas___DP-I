from tkinter.messagebox import NO
from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from django.views.generic import ListView, DetailView


# Create your views here.

def eventform(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        start_time = request.POST.get('start_time',None)
        end_time = request.POST.get('end_time', None)
        type = request.POST.get('type', '')
        genre = request.POST.get('genre', '')

        event= Event(name= name, start_time=start_time, end_time=end_time, type=type, genre=genre)
      
        event.save()
    return render(request, 'organization/eventform.html')



class EventsView(ListView):
    model= Event
    template_name = 'organization/events.html'

class EventDetail(DetailView):
    model= Event
    template_name= 'organization/eventDetail.html'