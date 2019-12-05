from rest_framework import serializers
from webapp.models import Project, Task


class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'project', 'summary', 'description', 'status', 'type', 'created_at', 'created_by',
                  'assigned_to')


class ProjectsSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'created_at', 'updated_at', 'tasks')



