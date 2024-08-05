from django.urls import path
from .views import*
from . import views

urlpatterns = [
    path('initiate/', views.initiate_payment, name='initiate'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_failure/', views.payment_failure, name='payment_failure'),
]
