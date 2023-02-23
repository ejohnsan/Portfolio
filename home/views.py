from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    
    return render(request, "home/index.html")

def portfolio(request):

    return render(request, "home/portfolio.html")

def about(request):
    
    return render(request, "home/about.html")