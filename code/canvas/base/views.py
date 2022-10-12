from django.shortcuts import render


def index(request):
    # return HttpResponse("Starting the project")
    return render(request, 'index.html')


<<<<<<< HEAD
=======
def user_auth(request):
    # return HttpResponse("Starting the project")
    return render(request, 'user_auth.html') 


def organization_auth(request):
    # return HttpResponse("Starting the project")
    return render(request, 'organization_auth.html') 
>>>>>>> 652687769a39ee0e027504e5a2eee535ec706f27
