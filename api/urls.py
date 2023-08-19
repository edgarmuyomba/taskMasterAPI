from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api'

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('tasks/', tasklist, name='task-list'),
    path('new-task/', newtask, name='new-task'),
    path('edit/<int:pk>/', edittask, name='update-task'),
    path('delete/<int:pk>/', deletetask, name='delete-task'),
    path('search/', search, name='search'),
]