from django.urls import path, include
from .views import*
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls.base import reverse_lazy

app_name = 'home'

urlpatterns = [
    path("",home, name="home"),  
    path("about/", views.about, name="about"),
    path("course/", views.course, name="course"),
    # path("vacancy/", views.vacancy_view, name="vacancy"),
    path('contact/', views.vacancy_view, name='contact'),
    path('message/', views.message, name='message'),
    path('coursedetail/', views.course_detail, name='coursedetail'),
    path('addtocart/', views.addtocart, name='addtocart'),
    
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
    
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('home:password_reset_confirm'), template_name="registration/passc.html"), 
         name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
] 
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)