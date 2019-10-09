from django.contrib import admin

from webapp.models import Task, Status, Type, Project

admin.site.register(Project)

admin.site.register(Task)

admin.site.register(Status)

admin.site.register(Type)
