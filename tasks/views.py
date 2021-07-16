from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import redirect
from django.urls import reverse_lazy

# serializers
from . api import serializers

# models
from tasks.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer
    queryset = Task.objects.all()

    # /api/tasks/{pk}/check-task/
    @action(detail=True, methods=['PUT'], url_path='check-task')
    def check_task(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk)
        task_serializer = serializers.TaskCheckSerializer(task, request.data)
        if task_serializer.is_valid():
            task_serializer.save()
            return redirect('/api/tasks/{}/'.format(task.pk))
        return Response({'Message': 'Error'}, status=status.HTTP_400_BAD_REQUEST)
