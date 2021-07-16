from django.db import models

# models
from tenants.models import TenantAware


# TenantAware 'sub_domain'
class Task(TenantAware):
    title = models.CharField('Título', max_length=100)
    description = models.TextField('Descrição')
    checked = models.BooleanField('Checado', default=False)
    update_at = models.DateTimeField('Data da atualização', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['title']


