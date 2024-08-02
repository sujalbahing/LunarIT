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
        return redirect('home/success.html')
    
    return render(request, 'home/vacancy.html')
    
    
# import ssl
# import certifi

# from django.shortcuts import render, redirect
# from .models import VacancyForm
# from django.core.mail import send_mail
# from django.conf import settings
# from django.contrib import messages
# from .models import *

# def home(request):
#     return render(request, 'home/homepage.html', {})

# def about(request):
#     abouts = About.objects.all()
#     return render(request, 'home/aboutpage.html', {'abouts': abouts})

# def course(request):
#     courses = Course.objects.all()
#     return render(request, 'home/coursepage.html', {'courses': courses})

# def contact(request):
#     return render(request, 'home/contactpage.html', {})

# def service1(request):
#     return render(request, 'home/servicepage1.html', {})

# def vacancy_view(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         message = request.POST.get('message')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         course_name = request.POST.get('course_name')

#         applicant = VacancyForm(name=name, phone=phone, email=email, message=message, course_name=course_name)
#         applicant.save()

#         ssl_context = ssl.create_default_context()
#         ssl_context.load_verify_locations(certifi.where())

#         send_mail(
#             'Application Received',
#             'Thank you for applying! Your application has been submitted successfully. We will contact you as soon as possible.',
#             settings.DEFAULT_FROM_EMAIL,
#             [email],
#             fail_silently=False,
#         )

#         messages.success(request, 'Your application has been submitted successfully!')
#         return redirect('home/success.html')

#     return render(request, 'home/vacancy.html')
