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

# services
from core.core_services import host_from_request


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer
    queryset = Task.objects.all()

    def list(self, request, *args, **kwargs):
        domain_prefix = host_from_request(request)
        tasks = Task.objects.filter(tenant__domain_prefix=domain_prefix)
        tasks_serializer = serializers.TaskSerializer(tasks, many=True, context={'request': request})
        return Response(tasks_serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        task = serializers.TaskCreateSerializer(data=request.data)
        if task.is_valid():
            task.save()
            return Response(task.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # /api/tasks/{pk}/check-task/
    @action(detail=True, methods=['PUT'], url_path='check-task')
    def check_task(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk)
        task_serializer = serializers.TaskCheckSerializer(task, request.data)
        if task_serializer.is_valid():
            task_serializer.save()
            return redirect('/api/tasks/{}/'.format(task.pk))
        return Response({'Message': 'Error'}, status=status.HTTP_400_BAD_REQUEST)
