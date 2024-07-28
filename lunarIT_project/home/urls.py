from django.urls import path, include
from .views import*
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path("",views.home, name="home"),  
    path("about/", views.about, name="about"),
    path("product/", views.product, name="product"),
    path("contact/", views.contact, name="contact"),
    path("service1/", views.service1, name="service1"),
    path("test/", views.test, name="test"),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)