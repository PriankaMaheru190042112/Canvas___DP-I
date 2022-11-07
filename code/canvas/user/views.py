from django.shortcuts import render
from events.models import User, Event,Image, Genre
from django.views.generic import ListView, DetailView
# Create your views here.
from django.utils.timezone import now

def user_auth(request):
    # return HttpResponse("Starting the project")
    return render(request, 'user/user_auth.html') 


def user_home(request):
    # return HttpResponse("Starting the project")
   objects= Event.objects.all()
   genres = Genre.objects.all()
   q= request.POST.get('genre')
   print(q)

   today = now().date()
   objects= Event.objects.filter(start_date__gte=today).order_by('start_date')[:5]
   print("blablabla")

   if q =="Photography":
        today = now().date()
        objects= Event.objects.filter(genre = q,start_date__gte=today ).order_by('start_date')[:3]
        print("boop")

   elif q=="Abstract Art":
        today = now().date()
        objects= Event.objects.filter(genre = q, start_date__gte=today ).order_by('start_date')[:3]
        print("nope")

   context={

        'genres': genres ,
        'objects': objects
    }

   return render(request, 'user/user_home.html',context) 


def user_profile(request):  
    # return HttpResponse("Starting the project")
    return render(request, 'user/user_profile.html') 


def user_gallery(request):
    # return HttpResponse("Starting the project")
    return render(request, 'user/user_gallery.html') 

class EventDetail(DetailView):
    model= Event
    template_name= 'user/event_details.html'    