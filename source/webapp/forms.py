from django import forms
from django.forms import widgets
from webapp.models import Status, Type, Task, Project


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['created_at']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['created_at', 'updated_at']


class ProjectTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description']