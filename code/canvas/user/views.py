from django.shortcuts import render
from events.models import Event,Image, Genre
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
        if (user is not None):
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


@login_required
def user_logout(request):  
    logout(request)
    # return HttpResponseRedirect(reverse('/user/user_home/'))
    return render(request, 'user/user_auth.html') 
    


def user_profile(request):  
    # return HttpResponse("Starting the project")
    return render(request, 'user/user_profile.html') 


def user_gallery(request):
    # return HttpResponse("Starting the project")
    return render(request, 'user/user_gallery.html') 

class EventDetail(DetailView):
    model= Event
    template_name= 'user/event_details.html'    