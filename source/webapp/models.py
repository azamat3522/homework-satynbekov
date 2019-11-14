from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


def get_admin():
    return User.objects.get(username='admin').id


class Project(models.Model):

    name = models.CharField(max_length=20, verbose_name='Названия проекта')

    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание проекта')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.name


class Task(models.Model):

    project = models.ForeignKey('webapp.Project', related_name='tasks', null=True, blank=False,
                                on_delete=models.PROTECT, verbose_name='Проект')

    summary = models.CharField(max_length=200, verbose_name='Заголовок')

    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')

    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT, related_name='tasks',
                               verbose_name='Статус')

    type = models.ForeignKey('webapp.Type', on_delete=models.PROTECT, related_name='tasks',
                             verbose_name='Тип')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    created_by = models.ForeignKey(User, null=False, blank=False, default=get_admin, verbose_name='Автор задачи',
                                   on_delete=models.PROTECT, related_name='tasks')

    assigned_to = models.ForeignKey(User, null=True, blank=False, verbose_name='Исполнитель задачи',
                                    on_delete=models.PROTECT, related_name='task')

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


class Team(models.Model):
    user = models.ForeignKey('auth.User', related_name='user_projects', on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    project = models.ForeignKey('webapp.Project', related_name='project_users', on_delete=models.CASCADE,
                                verbose_name='Проект')
    start_date = models.DateField(null=True, verbose_name='Дата начала работы')
    end_date = models.DateField(null=True, verbose_name='Дата окончания работы')

    def __str__(self):
        return "{} | {}".format(self.user, self.project)



