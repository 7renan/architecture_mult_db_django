from django.db import models


class Tenant(models.Model):
    name = models.CharField('Nome', max_length=100)
    domain_prefix = models.CharField('Prefixo do domínio', max_length=50)

    def __str__(self):
        return self.name


class TenantAware(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta:
        abstract = True
