from django.shortcuts import render


def index(request):
    # return HttpResponse("Starting the project")
    return render(request, 'index.html')


