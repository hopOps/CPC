from django.shortcuts import render, HttpResponse, loader


# Create your views here.
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'logon.html')


