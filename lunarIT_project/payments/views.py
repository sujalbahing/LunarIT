import requests
from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
from .models import Payment

def initiate_payment(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        payment = Payment.objects.create(user=request.user, amount=amount)

        esewa_payment_url = "https://uat.esewa.com.np/epay/main"
        success_url = request.build_absolute_uri(reverse('payment_success'))
        failure_url = request.build_absolute_uri(reverse('payment_failure'))

        context = {
            'amt': payment.amount,
            'pdc': 0,
            'psc': 0,
            'txAmt': 0,
            'tAmt': payment.amount,
            'pid': payment.id,
            'scd': settings.ESEWA_MERCHANT_CODE,
            'su': success_url,
            'fu': failure_url,
            'esewa_payment_url': esewa_payment_url
        }
        return render(request, 'payments/initiate_payment.html', context)
    return render(request, 'payments/initiate_payment.html')

def payment_success(request):
    oid = request.GET.get('oid')
    amt = request.GET.get('amt')
    refId = request.GET.get('refId')

    payment = Payment.objects.get(id=oid, amount=amt)

    url = "https://uat.esewa.com.np/epay/transrec"
    params = {
        'amt': amt,
        'rid': refId,
        'pid': oid,
        'scd': settings.ESEWA_MERCHANT_CODE,
    }

    response = requests.post(url, params=params)
    status = response.text.split('')[1]  # Adjust this based on the actual response structure

    if status == 'Success':
        payment.status = 'COMPLETED'
        payment.transaction_id = refId
        payment.save()
        return redirect('payment_success_page')
    else:
        payment.status = 'FAILED'
        payment.save()
        return redirect('payment_failure_page')

def payment_failure(request):
    return render(request, 'payments/failure.html')
