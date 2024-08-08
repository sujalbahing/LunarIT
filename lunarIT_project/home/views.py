from django.shortcuts import render, redirect, get_object_or_404
from .models import VacancyForm
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

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

def service1(request):
    return render(request, 'home/servicepage1.html', {})

def course_detail(request):
    return render(request, 'home/coursedetail.html')

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
        return redirect('/')
    
    return render(request, 'home/vacancy.html')