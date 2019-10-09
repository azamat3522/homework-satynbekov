from django.db import models


class Task(models.Model):

    summary = models.CharField(max_length=200, verbose_name='Заголовок')

    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')

    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT, related_name='tasks',
                               verbose_name='Статус')

    type = models.ForeignKey('webapp.Type', on_delete=models.PROTECT, related_name='tasks',
                             verbose_name='Тип')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.summary



class Status(models.Model):

    name = models.CharField(max_length=20, verbose_name='Название статуса')

    def __str__(self):
        return self.name

class Type(models.Model):

    name = models.CharField(max_length=20, verbose_name='Название типа')

    def __str__(self):
        return self.name



