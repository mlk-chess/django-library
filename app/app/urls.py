from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='bookseller_route'),
    path('', include('index.urls'), name='index'),
    path('register/', include('register.urls'), name='register'),
]