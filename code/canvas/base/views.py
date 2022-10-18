from django.shortcuts import render
from events.models import User,Organization, Event,Image
# Create your views here.
from django.utils.timezone import now


def index(request):
    # return HttpResponse("Starting the project")
    objects = Event.objects.all()
    today = now().date()
    objects= Event.objects.filter(start_date__gte=today).order_by('start_date')[:3]
    
    return render(request, 'index.html',{'objects':objects}) 


