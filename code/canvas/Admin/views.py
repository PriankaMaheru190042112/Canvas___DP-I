from django.shortcuts import render

# Create your views here.
def Admin_auth(request):  
    # return HttpResponse("Starting the project")
    return render(request, 'Admin/Admin_auth.html') 