from django.urls import path
from .views import *

app_name = 'library'

urlpatterns = [
    path('', library_list, name='library_list'),
    path('detail/<int:library_id>/', library_detail, name='library_detail'),
]
