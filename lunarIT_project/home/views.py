from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from .models import Course


def home(request):
    return render(request, 'home/homepage.html', {})

def about(request):
    return render(request, 'home/aboutpage.html', {})

def product(request):
    return render(request, 'home/productpage.html', {})

def contact(request):
    
    return render(request, 'home/contactpage.html', {})

def service1(request):
    return render(request, 'home/servicepage1.html', {})

def test(request):
    courses = Course.objects.all()
    return render(request, 'home/test.html', {'courses': courses})
