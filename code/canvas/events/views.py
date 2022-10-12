from http.client import ImproperConnectionState
import imp
from django.shortcuts import render
from .models import Event
from django.views.generic import ListView, DetailView
# Create your views here.


class EventListView(ListView):
    model= Event
    template_name = 'events/main.html'


class EventDetailView(DetailView):
    model= Event
    template_name= 'events/countdown.html'