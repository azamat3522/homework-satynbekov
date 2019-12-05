from rest_framework import viewsets

from api.serializers import ProjectsSerializer, TaskSerializer
from webapp.models import Project, Task


class ProjectViewset(viewsets.ModelViewSet):
    serializer_class = ProjectsSerializer
    queryset = Project.objects.all()


class TaskViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()



