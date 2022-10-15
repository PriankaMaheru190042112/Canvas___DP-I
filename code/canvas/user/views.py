from django.shortcuts import render

# Create your views here.


def user_auth(request):
    # return HttpResponse("Starting the project")
    return render(request, 'user/user_auth.html') 


def user_home(request):
    # return HttpResponse("Starting the project")
    return render(request, 'user/user_home.html') 


def user_profile(request):
    # return HttpResponse("Starting the project")
    return render(request, 'user/user_profile.html') 

def user_gallery(request):
    # return HttpResponse("Starting the project")
    return render(request, 'user/user_gallery.html') 