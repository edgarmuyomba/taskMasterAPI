from django.shortcuts import render
from rest_framework import generics 
from tasks.serializers import TaskSerializer
from rest_framework.response import Response
from tasks.models import *
from rest_framework.decorators import api_view

@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(data=serializer.data)

@api_view(['POST'])
def newtask(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=200)
        
@api_view(['PUT'])
def edittask(request, pk):
    pass