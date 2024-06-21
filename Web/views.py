from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def courses(request):
    return render(request, 'courses.html')

def register(request):
    return render(request, 'register.html')