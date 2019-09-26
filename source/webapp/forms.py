from django import forms
from django.forms import widgets
from webapp.models import Status, Type

class TaskForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label='Summary')
    description = forms.CharField(max_length=2000, required=False, label='Description',
                                  widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Status')
    type = forms.ModelChoiceField(queryset=Type.objects.all(), label='Type')


class StatusForm(forms.Form):
    name = forms.CharField(max_length=20, required=True, label='Status_name')


class TypeForm(forms.Form):
    name = forms.CharField(max_length=20, required=True, label='Type_name')
