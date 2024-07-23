from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home/homepage.html', {})

def about(request):
    return render(request, 'home/aboutpage.html', {})

def product(request):
    return render(request, 'home/productpage.html', {})

def contact(request):
    return render(request, 'home/contactpage.html', {})

def authView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("login:login")
    else:
        form = UserCreationForm( )
    return render(request,'registration/signup.html', {'form': form})