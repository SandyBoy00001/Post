# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Welcome to my homepage")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("Welcome to my about page")
    return render(request, 'about.html')