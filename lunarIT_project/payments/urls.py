from django.urls import path
from .views import*
from . import views

urlpatterns = [
    path('initiate/', views.initiate_payment, name='initiate_payment'),
    path('esewa-verify/', views.esewa_verify, name='esewa_verify'),
]
