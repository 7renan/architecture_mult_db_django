from rest_framework import serializers

# models
from tasks.models import Task
# serializers
from tenants.api.serializers import TenantSerializer


class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['tenant', 'id', 'title', 'checked', 'description', 'update_at',]


class TaskSerializer(serializers.ModelSerializer):

    tenant = TenantSerializer(many=False, read_only=True)

    class Meta:
        model = Task
        fields = ['tenant', 'id', 'title', 'checked', 'description', 'update_at', ]


class TaskCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['checked']