import random
from django.shortcuts import render
from events.models import Event,Image, Genre,Participant
from django.views.generic import ListView, DetailView
# Create your views here.
from django.utils.timezone import now
from .forms import CreateUserForm
from authentication_user.models import User
from django.contrib.auth import login, authenticate ,logout
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.db.models import Count, F

def registerlogin(request):
    # return HttpResponse("Starting the project")
    form = CreateUserForm()
    if request.method == 'POST' and 'registerbtn' in request.POST:
        form = CreateUserForm(request.POST)
        email = request.POST.get('email')
    
        if form.is_valid():
            form.save()
            uobj2 = User.objects.get(email=email)  
            uobj2.isAdmin = False
            uobj2.isUser = True
            uobj2.isOrganization = False
            uobj2.save()

    elif request.method=='POST' and 'loginbtn' in request.POST:
        #email= request.POST.get('email')
        name= request.POST.get('name')
        password = request.POST.get('password')  
        print("done")
        user = authenticate(request, username=name , password = password)
        if (user is not None and user.isUser==True):
                login(request, user)
                print("success")
                return redirect('/user/user_home/')
                
        else:
                # messages.info(request, "Username or Password is incorrect.")
                print("error")

    context = {'form': form }
    return render(request,"user/user_auth.html", context) 

    

@login_required
def user_home(request):
    # return HttpResponse("Starting the project")
   objects= Event.objects.all()
   genres = Genre.objects.all()
   participants= Participant.objects.filter(participant_name= request.user.username)

   print(participants)
   if(participants):
    flag=1
   else:
    flag=0 

   q= request.POST.get('genre')
   today = now().date()
   objects= Event.objects.filter(start_date__gte=today).order_by('start_date')[:5]
   

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
        'objects': objects,
        'participants': participants,
        'flag': flag
    }

   

   if request.method == 'POST' and 'paybtn' in request.POST:
    ename=request.POST.get('ename')
    print(ename)

    current_user =request.user.username
    print(current_user)  
    code = random.randint(1000,2000)
    print(code)
    
    participant= Participant.objects.create(participant_name=current_user, event_name= ename, code=code)
    participant.save()


   if request.method == 'POST' and 'pubbtn' in request.POST:
    pub=request.POST.get('pub')
    print(pub)

    current_user =request.user.username
    print(current_user)  
    code = 0
    print(code)
    
    participant= Participant.objects.create(participant_name=current_user, event_name= pub, code=code)
    participant.save()
   
   

   return render(request, 'user/user_home.html',context) 


@login_required
def user_logout(request):  
    logout(request)
    # return HttpResponseRedirect(reverse('/user/user_home/'))
    return render(request, 'user/user_auth.html') 
    


def user_profile(request):  

    current_user = request.user.username
    u_info = User.objects.all()
    if request.method == 'POST' and 'update_pass_btn' in request.POST:
       pass1= request.POST.get('pass1')
       pass2= request.POST.get('pass2')

       u = authenticate(request, username=current_user, password = pass1)
       if (u is not None and u.isUser==True):
           print("vhjfvjehfjj")
           u.password= make_password(pass2)
           u.save()
    
    elif request.method == 'POST' and 'update_img_btn' in request.POST:

        pro_img= request.POST.get('pro_img')
        u = User.objects.get(username= current_user)
        u.profile_picture = pro_img
        u.save()

    context={
        'u_info' : u_info
    }

    return render(request, 'user/user_profile.html',context) 


def user_gallery(request):
    # return HttpResponse("Starting the project")
    return render(request, 'user/user_gallery.html') 

    

class EventDetail(DetailView):
    model= Event
    template_name= 'user/event_details.html' 

    # queryset= Event.objects.filter()
    context_object_name= 'event_id'
    
    def get_context_data(self, **kwargs):
        context=super(EventDetail,self).get_context_data(**kwargs)
        context['image']= Image.objects.filter(event_id= self.object)
        return context



def user_cart(request,pk):
    e = Event.objects.filter(event_id= pk)
    print(e[0])
    img= Image.objects.filter(event_id= e[0])
    print(img)
    
    context={
        'e': e[0] ,
        'img':img
    }
    return render(request, 'user/user_cart.html', context)

def user_virtual_box(request,pk):
    e = Event.objects.filter(event_id= pk)
    print(e[0])
    img= Image.objects.filter(event_id= e[0])
    context={
        'e': e[0] ,
        'img':img
    }
    return render(request, 'user/user_virtual_box.html',context)        


def user_join_form(request,pk):
    e = Event.objects.filter(event_id= pk)

    if request.method == "POST":
        name = request.POST.get('name')
        code = request.POST.get('code')
        eid= request.POST.get('eid')
        print(name)
        print(code)
        
        join = Participant.objects.get(participant_name= name, code=code)

        if(join):
            print(join.participant_id)
            print(eid)
            return redirect('user:event_detail', eid)
           



    return render(request, 'user/user_join_form.html', {'e': e[0]})

    