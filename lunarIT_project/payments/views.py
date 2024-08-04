import requests
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Payment

def initiate_payment(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        order_id = 'your_unique_order_id'  # Generate a unique order ID
        payment = Payment.objects.create(order_id=order_id, amount=amount)
        context = {
            'payment': payment,
            'merchant_id': 'your_merchant_id',
            'return_url': 'http://127.0.0.1:8000/payments/esewa-verify/',  # Update with your verify URL
            'cancel_url': 'http://127.0.0.1:8000/payments/esewa-cancel/',  # Update with your cancel URL
            'esewa_url': 'https://esewa.com.np/epay/main'
        }
        return render(request, 'payments/initiate_payment.html', context)
    return render(request, 'payments/initiate_payment.html')

def esewa_verify(request):
    if request.method == 'GET':
        ref_id = request.GET.get('refId')
        oid = request.GET.get('oid')
        amount = request.GET.get('amt')

        url = 'https://esewa.com.np/epay/transrec'
        params = {
            'amt': amount,
            'rid': ref_id,
            'pid': oid,
            'scd': 'your_merchant_id'
        }
        response = requests.post(url, data=params)
        status = response.text

        if 'Success' in status:
            payment = Payment.objects.get(order_id=oid)
            payment.esewa_ref_id = ref_id
            payment.save()
            return render(request, 'payments/success.html')
        else:
            return render(request, 'payments/failure.html')
    return redirect('home')
