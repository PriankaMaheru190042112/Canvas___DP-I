from multiprocessing import context
from django.shortcuts import render
from events.models import User,Organization, Event,Image, Genre
# Create your views here.
from django.utils.timezone import now


def index(request):
    objects= Event.objects.all()
    genres = Genre.objects.all()
    q= request.POST.get('genre')
    print(q)
    
    # if q=="All":
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
    
    return render(request, 'index.html',context) 


