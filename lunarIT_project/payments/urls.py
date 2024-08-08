from django.urls import path
from .views import*
from . import views

urlpatterns = [
    path('customer/', views.customer_list, name='customer'),
    path('course/verify_payment/', views.verify_payment, name='verify_payment'),
]
