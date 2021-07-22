from django.contrib import admin

# models
from .models import Task

# services
from core.core_services import host_from_request

admin.site.register(Task)


class TaskAdmin(admin.ModelAdmin):
    fields = ['title', 'description']

    def get_queryset(self, request, *args, **kwargs):
        queryset = super().get_queryset(request, *args, **kwargs)
        tenant = host_from_request(request)
        queryset = queryset.filter(tenant=tenant)
        return queryset
