from django.shortcuts import render, redirect

# Create your views here.

def index_view(request):
    return render(request, "home/index.html")

def leadership_view(request):
    return render(request, "home/leadership.html")

def mun101_view(request):
    return render(request, "home/mun101.html")

def calendar_view(request):
    return render(request, "home/calendar.html")

