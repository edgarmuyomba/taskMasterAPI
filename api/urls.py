from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('tasks/', tasklist, name='task-list'),
    path('new-task/', newtask, name='new-task'),
    path('edit/<int:pk>/', edittask, name='update-task'),
]