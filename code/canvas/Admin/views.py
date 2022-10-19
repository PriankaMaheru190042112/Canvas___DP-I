from django.shortcuts import render

# Create your views here.
def Admin_auth(request):  
    # return HttpResponse("Starting the project")
    return render(request, 'Admin/Admin_auth.html') 


def Admin_home(request):  
    # return HttpResponse("Starting the project")
    return render(request, 'Admin/Admin_home.html') 


def Admin_profile(request):  
    # return HttpResponse("Starting the project")
    return render(request, 'Admin/Admin_profile.html') 