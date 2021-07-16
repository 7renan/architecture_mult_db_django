from django.shortcuts import render
from rest_framework import viewsets
# models
from .models import Tenant

# serializers
from tenants.api import serializers


class TenantViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TenantSerializer
    queryset = Tenant.objects.all()
