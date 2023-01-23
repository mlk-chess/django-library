from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import profile

urlpatterns = [
    path('', include('index.urls'), name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('register/', include('register.urls'), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login/index.html'), name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]