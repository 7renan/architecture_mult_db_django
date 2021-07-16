from rest_framework import serializers

# models
from tenants.models import Tenant


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ('id', 'name', 'domain_prefix')