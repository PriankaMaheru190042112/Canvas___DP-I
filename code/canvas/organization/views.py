from importlib.resources import path
from multiprocessing import AuthenticationError
from tkinter.messagebox import NO
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from events.models import Image
from .models import Event,Image,User,Organization
from django.views.generic import ListView, DetailView
from cryptography.fernet import Fernet
from django.core.mail import EmailMessage
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

        # org = authenticate(request, email=email, password= encryptPassword(password))
        if orgs is not None:
            # login(request, org)
            print("login successful")
            return HttpResponseRedirect("/organization/eventlist")

        else:
            print("login failed")    
            
    form = AuthenticationForm()
    return render(request=request,template_name="organization/organization_auth.html", context={"login_form":form}) 



class EventsView(ListView):
    model= Event
    template_name = 'organization/events.html'

class EventDetail(DetailView):
    model= Event
    template_name= 'organization/eventDetail.html'