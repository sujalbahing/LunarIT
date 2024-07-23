from django.urls import path, include
from .views import*
from . import views

urlpatterns = [
    path("",views.home, name="home"),  
    path("about/", views.about, name="about"),
    path("product/", views.product, name="product"),
    path("contact/", views.contact, name="contact"),
    path("signup/", authView, name="authView"),
    path("", include("django.contrib.auth.urls")),
]