from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Customer
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required

import random
import string
import uuid
import requests
import json
import time


def customer_list(request):
    course_name = ""
    course_price = 0
    if request.method == 'POST':
        course_name = request.POST.get('course', '')

        if course_name:
            # Fetch the course price from the database
            course = get_object_or_404(Course, Name=course_name)
            course_price = course.Price * 100

        if 'firstName' in request.POST:
            firstName = request.POST.get('firstName')
            lastName = request.POST.get('lastName')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            course = request.POST.get('course')
            payment = request.POST.get('payment')  # Handle file upload
            amount = request.POST.get('amount')
            password = generate_random_password()
            url = "https://a.khalti.com/api/v2/epayment/initiate/"
            return_url = request.build_absolute_uri('/payments/course/verify_payment/')
            website_url = request.POST.get('return_url')
            purchase_order_id = generate_purchase_order_id()

            payload = json.dumps({
                "return_url": return_url,
                "website_url": website_url,
                "amount": int(float(amount) * 100),
                "purchase_order_id": purchase_order_id,
                "purchase_order_name": "test",
                "customer_info": {
                    "name": firstName + " " + lastName,
                    "email": email,
                    "phone": phone
                }
            })
            
            headers = {
                'Authorization': 'Key 805a1ce5f95740ff927c01b65d518f3c',
                'Content-Type': 'application/json',
            }

            print("Payload:", payload)
            print("Headers:", headers)

            try:
                response = requests.post(url, headers=headers, data=payload)
                print("Response:", response.text)
                response.raise_for_status()  # Raise HTTPError for bad responses
                new_res = response.json()

                if 'payment_url' in new_res:
                    # Save necessary data to the session for later use
                    request.session['firstName'] = firstName
                    request.session['lastName'] = lastName
                    request.session['email'] = email
                    request.session['phone'] = phone
                    request.session['course'] = course
                    request.session['payment'] = payment
                    request.session['amount'] = amount
                    request.session['password'] = password
                    request.session['purchase_order_id'] = purchase_order_id

                    return redirect(new_res['payment_url'])

                else:
                    return HttpResponse("Error: 'payment_url' not found in the response", status=500)

            except requests.exceptions.RequestException as e:
                return HttpResponse(f"Error: Failed to initiate payment - {e}", status=500)

    return render(request, 'payments/customer.html', {'course_name': course_name, 'course_price': course_price})

@csrf_exempt
def verify_payment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
    elif request.method == 'GET':
        data = request.GET

    if data.get('status') == 'Completed':
        # Retrieve data from the session
        firstName = request.session.get('firstName')
        lastName = request.session.get('lastName')
        email = request.session.get('email')
        phone = request.session.get('phone')
        course = request.session.get('course')
        payment = request.session.get('payment')
        amount = request.session.get('amount')
        amount = int(float(amount) / 100)
        password = request.session.get('password')
        purchase_order_id = request.session.get('purchase_order_id')
        print(amount)
        # Fetch the course object
        course_obj = get_object_or_404(Course, Name=course)

        # Create the user
        user = User(username=email, first_name=firstName, last_name=lastName, email=email, password=make_password(password))
        user.save()

        # Create the customer
        customer = Customer(user=user, course=course_obj, phone=phone, amount=amount, payment=payment, purchase_order_id=purchase_order_id)
        customer.save()

        # Email content
        subject = 'Your Login Credentials'
        message = f'Hello {firstName},\n\nYour login credentials are as follows:\n\nEmail: {email}\nPassword: {password}\n\nPlease keep this information safe.'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email]

        # Send email
        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False,
        )

        if request.method == 'POST':
            # return JsonResponse({'message': 'Payment verified and customer created successfully'}, status=200)
            return redirect('course')

        else:
            # return HttpResponse('Payment verified and customer created successfully', status=200)
            return redirect('course')
    else:
        if request.method == 'POST':
            return JsonResponse({'message': 'Payment verification failed'}, status=400)
        else:
            return HttpResponse('Payment verification failed', status=400)

def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_purchase_order_id(base='ID'):
    random_number = ''.join(random.choices(string.digits, k=4))
    return f'{base}{random_number}'