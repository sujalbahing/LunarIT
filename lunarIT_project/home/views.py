from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from .models import *


def home(request):
    return render(request, 'home/homepage.html', {})

def about(request):
    abouts = About.objects.all()
    return render(request, 'home/aboutpage.html', {'abouts': abouts})

def course(request):
    courses = Course.objects.all()
    return render(request, 'home/coursepage.html', {'courses': courses})

def contact(request):
    
    return render(request, 'home/contactpage.html', {})

def service1(request):
    return render(request, 'home/servicepage1.html', {})

