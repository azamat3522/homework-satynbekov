from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from webapp.models import Status, Type, Task, Project, Team


class TaskForm(forms.ModelForm):
    def __init__(self, project, **kwargs):
        super().__init__(**kwargs)
        self.fields['assigned_to'].queryset = User.objects.filter(
            user_projects__project__in=project
        )

    class Meta:
        model = Task
        exclude = ['created_at', 'created_by', 'project']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']


class ProjectForm(forms.ModelForm):

    user = forms.ModelMultipleChoiceField(queryset=User.objects.all())

    class Meta:
        model = Project
        exclude = ['created_at', 'updated_at']


class ProjectTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class TeamUpdateForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['team_users'] = forms.ModelMultipleChoiceField(queryset=User.objects.all(),
                                                                   initial=self.initial.get('team'),
                                                                   required=False
                                                                   )


# class TeamForm(forms.ModelForm):
#     class Meta:
#         model = Team
#         fields = [ 'user', 'project', 'start_date', 'end_date']


