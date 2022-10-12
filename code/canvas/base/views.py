from django.shortcuts import render


def index(request):
    # return HttpResponse("Starting the project")
    return render(request, 'index.html')


def user_auth(request):
    # return HttpResponse("Starting the project")
    return render(request, 'user_auth.html') 


def organization_auth(request):
    # return HttpResponse("Starting the project")
    return render(request, 'organization_auth.html') 