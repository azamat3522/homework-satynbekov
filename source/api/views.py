from rest_framework import viewsets
from rest_framework.permissions import AllowAny, SAFE_METHODS, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import ProjectsSerializer, TaskSerializer
from webapp.models import Project, Task


class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})


class ProjectViewset(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = ProjectsSerializer
    queryset = Project.objects.all()

    # def get_permissions(self):
    #     if self.request.method in SAFE_METHODS:
    #         return []
    #     return super().get_permissions()


class TaskViewset(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()



