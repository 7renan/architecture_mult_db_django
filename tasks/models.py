from django.db import models


class Task(models.Model):
    title = models.CharField('Título', max_length=100)
    description = models.TextField('Descrição')
    checked = models.BooleanField('Checado', default=False)
    update_at = models.DateTimeField('Data da atualização', auto_now=True)

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['title']

    def __str__(self):
        self.title
