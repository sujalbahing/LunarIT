from django.urls import path, include
from .views import*
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import vacancy_view
from django.views.generic import TemplateView

urlpatterns = [
    path("",views.home, name="home"),  
    path("about/", views.about, name="about"),
    path("course/", views.course, name="course"),
    path("contact/", views.contact, name="contact"),
    path("service1/", views.service1, name="service1"),
    path('vacancy/', views.vacancy_view, name='vacancy'),
    path('success/', TemplateView.as_view(template_name='home/success.html'), name='success'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)