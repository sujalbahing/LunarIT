from django.urls import path
from .import views

urlpatterns = [
    path('course/verify_payment/', views.verify_payment, name='verify_payment'),
    path('checkout/', views.checkout, name='checkout'),
]
