from django.urls import path
from .views import*
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path("",views.home, name="home"),  
    path("about/", views.about, name="about"),
    path("course/", views.course, name="course"),
    path("contact/", views.contact, name="contact"),
    path('vacancy/', views.vacancy_view, name='vacancy'),
    path('message/', views.message, name='message'),
    path('coursedetail/', views.course_detail, name='coursedetail'),
    path('addtocart/', views.addtocart, name='addtocart'),
    
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)