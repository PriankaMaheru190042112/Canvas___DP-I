from django.shortcuts import render

# Create your views here.


def user_auth(request):
    # return HttpResponse("Starting the project")
    return render(request, 'user/user_auth.html') 