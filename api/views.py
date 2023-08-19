from tasks.serializers import TaskSerializer
from rest_framework.response import Response
from tasks.models import *
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all().filter(owner=request.user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(data=serializer.data)

@api_view(['POST'])
def newtask(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=200)
        
@api_view(['PUT', 'PATCH'])
def edittask(request, pk):
    instance = get_object_or_404(Task, pk=pk)
    serializer = TaskSerializer(instance=instance, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(data=serializer.data)
    
@api_view(['DELETE'])
def deletetask(request, pk):
    instance = get_object_or_404(Task, pk=pk)
    if instance:
        instance.delete()
        return Response({"success": "task deleted"})
    return Response({"error": "failed to delete task"})
    
@api_view(['GET'])
def search(request):
    query = request.GET.get('query', None)
    if query:
        results = Task.objects.search(query).filter(owner=request.user)
        serializer = TaskSerializer(results, many=True)
        return Response(data=serializer.data)