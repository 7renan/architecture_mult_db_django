from rest_framework import serializers

# models
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title', 'checked', 'description', 'update_at', ]


class TaskCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['checked']