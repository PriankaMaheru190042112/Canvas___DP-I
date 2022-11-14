from email.mime import image
from importlib.resources import path
from multiprocessing import AuthenticationError
from tkinter.messagebox import NO
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, authenticate ,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from events.models import Event, Image
from authentication_user.models import User
from django.views.generic import ListView, DetailView
from cryptography.fernet import Fernet
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage

from .forms import CreateUserForm,EventForm
# Create your views here.

@login_required
def eventform(request):
   
    if request.method == "POST":
        name = request.POST.get('name', '')
        desc = request.POST.get('description')
        start_date= request.POST.get('start_date',None)
        start_time = request.POST.get('start_time',None)
        end_date= request.POST.get('end_date',None)
        end_time = request.POST.get('end_time', None)
        fee= request.POST.get('fees')
        genre = request.POST.get('genre')

        images= request.FILES.getlist('images')
        img_price = request.POST.get('img_price')
        frame_width= request.POST.get('frame_w')
        frame_height= request.POST.get('frame_h') 
        print(name)
        event= Event.objects.create(name= name, description= desc, start_date=start_date ,start_time=start_time, end_date=end_date ,end_time=end_time,
                     fee=fee, genre=genre)
        
        event.save()

        
        for i in images:
               e= Event.objects.get(name = name)
               image = Image.objects.create(event_id= e, image=i, img_price= img_price, frame_height= frame_height ,frame_width = frame_width)
            #    event.image = image
               image.save() 
        
    
        
        

    return render(request, 'organization/eventform.html')




def registerlogin(request):
    # return HttpResponse("Starting the project")
    form = CreateUserForm()
    if request.method == 'POST' and 'registerbtn' in request.POST:
        form = CreateUserForm(request.POST)
        # username = request.POST.get('username')
        email = request.POST.get('email')
        # password1 = request.POST.get('password1')
        if form.is_valid():
            form.save()
            uobj = User.objects.get(email=email)    
            uobj.isAdmin = False
            uobj.isUser = False
            uobj.isOrganization = True
            uobj.save()

    elif request.method=='POST' and 'loginbtn' in request.POST:
        # email= request.POST.get('email')
        name= request.POST.get('name')
        password = request.POST.get('password')  
        print("done")
        org = authenticate(request, username= name , password = password)
        if (org is not None):
                login(request, org)
                print("success")
                return redirect('/organization/organization_home/')
                
        else:
                # messages.info(request, "Username or Password is incorrect.")
                print("error")

    context = {'form': form }
    return render(request,"organization/organization_auth.html", context) 

    

@login_required
def organization_home(request):
    # return HttpResponse("Starting the project")
    objects = Event.objects.all()
    return render(request, 'organization/organization_home.html',{'objects':objects}) 

@login_required
def organization_logout(request):  
    logout(request)
    # return HttpResponseRedirect(reverse('/user/user_home/'))
    return render(request, 'organization/organization_auth.html') 
        
    
def organization_profile(request):
    # return HttpResponse("Starting the project")
    return render(request, 'organization/organization_profile.html') 


def organization_event(request):
    # return HttpResponse("Starting the project")
    return render(request, 'organization/organization_event.html') 


class EventsView(ListView):
    model= Event
    template_name = 'organization/events.html'

class EventDetail(DetailView):
    model= Event
    template_name= 'organization/eventDetail.html'