from email.mime import image
from importlib.resources import path
from multiprocessing import AuthenticationError
from tkinter.messagebox import NO
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from events.models import User,Organization,Event, Image
from django.views.generic import ListView, DetailView
from cryptography.fernet import Fernet
from django.core.mail import EmailMessage
# Create your views here.

def eventform(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        desc = request.POST.get('description')
        start_date= request.POST.get('start_date',None)
        start_time = request.POST.get('start_time',None)
        end_date= request.POST.get('end_date',None)
        end_time = request.POST.get('end_time', None)
        frame_width= request.POST.get('frame_w')
        frame_height= request.POST.get('frame_h') 
        fee= request.POST.get('fees')
        genre = request.POST.get('genre')
        images= request.FILES.get('images')
        img_price = request.POST.get('img_price')
        event= Event(name= name, description= desc, start_date=start_date ,start_time=start_time, end_date=end_date ,end_time=end_time, frame_width=frame_width,
                    frame_height=frame_height, fee=fee, genre=genre, img_path=images, img_price=img_price)


        event.save()

    return render(request, 'organization/eventform.html')


def encryptPassword(password):
        key= Fernet.generate_key()
        fernet= Fernet(key)
        encpassword = fernet.encrypt(password.encode())
        return encpassword

def decryptPassword(password):
        key= Fernet.generate_key()
        fernet= Fernet(key)
        encpassword = fernet.encrypt(password.decode())
        return encpassword


def register(request):
    # return HttpResponse("Starting the project")
    if request.method=='POST' and 'registerbtn' in request.POST:
        name= request.POST.get('name')
        email= request.POST.get('email')
        password= request.POST.get('password')
        confirmpass= request.POST.get('confirmpass')
        # hashed_pass= make_password(password)
        
        if(password == confirmpass):
            password= encryptPassword(password)
            organization= Organization(name= name, email=email, password=password)

            organization.save()
        else:
          print("password doesn't match") 
    
       # temp = "organization/organization_auth.html"
        return render(request, 'organization/organization_auth.html') 


    elif request.method=='POST' and 'loginbtn' in request.POST:
        email= request.POST.get('email')
        password = request.POST.get('password')
        orgs= Organization.objects.filter(email = email,password= encryptPassword(password))

        org = authenticate(request, email=email, password= encryptPassword(password))
        if orgs is not None:
            login(request, org)
            print("login successful")
            return HttpResponseRedirect("/organization/organization_home",{'orgs':orgs})

        else:
            print("login failed")    
            
    form = AuthenticationForm()
    return render(request=request,template_name="organization/organization_auth.html", context={"login_form":form}) 

    



def organization_home(request):
    # return HttpResponse("Starting the project")
    objects = Event.objects.all()
    return render(request, 'organization/organization_home.html',{'objects':objects}) 
    
    
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