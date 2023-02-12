from django.urls import path
from .views import *

app_name = 'group'

urlpatterns = [
    path('', group_list, name='group_list'),
    path('create/', group_create, name='group_create'),
    path('update/<int:id>/', group_update, name='group_update'),
    path('delete/<int:id>/', group_delete, name='group_delete'),
    path('<int:group_id>/', group_details, name='group_details'),
    path('<int:group_id>/join/', join_group, name='join_group'),
]
