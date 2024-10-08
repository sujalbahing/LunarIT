from django.shortcuts import render, redirect, get_object_or_404
from .models import VacancyForm
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordResetForm

@login_required
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

def message(request):
    return render(request, 'home/messagepage.html', {})

def course_detail(request):
    return render(request, 'home/coursedetail.html')

@login_required
def addtocart(request):
    return render(request, 'home/addtocart.html')


def vacancy_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')   
        course_name = request.POST.get('course_name')
        message = request.POST.get('message') 
        # print(message)

        applicant = VacancyForm(name=name, email=email, phone=phone, course_name=course_name, message=message)
        applicant.save()

         # Send confirmation email to the user
        send_mail(
            'Application Received',
            'Thank you for applying! Your application has been submitted successfully. We will contact you as soon as possible.',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        messages.success(request, 'Your application has been submitted successfully!')
        return redirect("home:message")
    
    return render(request, 'home/contactpage.html')

def authView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("home:login")
        else:
            messages.error(request, "Error creating account. Please check the form.")
    else:
        form = UserCreationForm( )
    return render(request,'registration/signup.html', {'form': form})


class CustomPasswordResetView(auth_views.PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'registration/pass.html'
    
class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'registration/passd.html'
    