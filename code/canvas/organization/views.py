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
from events.models import Event, Images,Genre
from authentication_user.models import User
from django.views.generic import ListView, DetailView
from cryptography.fernet import Fernet
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from .forms import CreateUserForm
# Create your views here.

@login_required
def eventform(request):
    current_user= request.user.username 
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('description')
        start_date= request.POST.get('start_date',None)
        # start_time = request.POST.get('start_time',None)
        end_date= request.POST.get('end_date',None)
        # end_time = request.POST.get('end_time', None)
        fee= request.POST.get('fees')
        genre = request.POST.get('genre')

        images= request.FILES.getlist('images')
        img_price = request.POST.get('img_price')
        frame_width= request.POST.get('frame_w')
        frame_height= request.POST.get('frame_h') 
        
        event= Event.objects.create(org=request.user.username, name= name, description= desc, start_date=start_date , end_date=end_date ,
                     fee=fee, genre=genre)
        
        print(images)

        
        for i in images:
        
               image = Images.objects.create(event_id= event, image=i, img_price= img_price, frame_height= frame_height ,frame_width = frame_width)

               image.save() 
        
        event.save()
        return redirect('/organization/organization_home/')
        
        

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
        org = authenticate(request, username= name , password = password)
        if (org is not None and org.isOrganization==True):
                login(request, org)
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
    pending = Event.objects.filter(is_accepted=False, is_rejected= False)
    accepted= Event.objects.filter(is_accepted= True, is_rejected= False)
    rejected= Event.objects.filter(is_accepted= False, is_rejected=True)

    context={
     'objects' : objects,
     'pending' : pending,
     'accepted' : accepted,
     'rejected' : rejected
    }
    return render(request, 'organization/organization_home.html',context) 

@login_required
def organization_logout(request):  
    logout(request)
    # return HttpResponseRedirect(reverse('/user/user_home/'))
    return render(request, 'organization/organization_auth.html') 
        
    
def organization_profile(request):
    current_user = request.user.username
    u_info = User.objects.all()
    if request.method == 'POST' and 'update_pass_btn' in request.POST:
       pass1= request.POST.get('pass1')
       pass2= request.POST.get('pass2')

       u = authenticate(request, username=current_user, password = pass1)
       if (u is not None and u.isOrganization==True):
           u.password= make_password(pass2)
           u.save()
    
    elif request.method == 'POST' and 'update_img_btn' in request.POST:

        pro_img= request.FILES.get('pro_img')
        print(pro_img)
        u = User.objects.get(username= current_user)
        print(u)
        u.profile_picture = pro_img
        u.save()

    context={
        'u_info' : u_info
    }

    return render(request, 'organization/organization_profile.html',context) 


def organization_event(request):
    # return HttpResponse("Starting the project")
    return render(request, 'organization/organization_event.html') 


class EventsView(ListView):
    model= Event
    template_name = 'organization/events.html'

class EventDetail(DetailView):
    model= Event
    template_name= 'organization/eventDetail.html'

    context_object_name= 'event_id'
    
    def get_context_data(self, **kwargs):
        context=super(EventDetail,self).get_context_data(**kwargs)
        context['image']= Images.objects.filter(event_id= self.object)
        return context