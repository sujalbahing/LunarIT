from django.shortcuts import render, redirect
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

def service1(request):
    return render(request, 'home/servicepage1.html', {})

def vacancy_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        email = request.POST.get('email')   
        phone = request.POST.get('phone')
        course_name = request.POST.get('course_name') 
        # print(message)
        
        applicant = VacancyForm(name=name, phone=phone, email=email, message=message, course_name=course_name)
        applicant.save()
        
        send_mail(
            'Application Received',
            'Thank you for applying! Your application has been submitted successfully. We will contact you as soon as possible.',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        
        # messages.success(request, 'Your application has been submitted successfully!')
        # return redirect('home/success.html')
    
    return render(request, 'home/vacancy.html')



# Send confirmation email to the user
    #     send_mail(
    #             'Course Enrollment Confirmation',
    #             f'Thank you for enrolling in {course_name}. We will contact you soon.',
    #             'Sujal.rai147@gmail.com',  # Replace with your email
    #             [email],
    #             fail_silently=False,
    #         )
    #     # return redirect('home/success.html')  # Redirect to a success page
        
    # return render(request, 'home/vacancy.html')