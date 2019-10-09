from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import TaskForm
from webapp.models import Task



class IndexView(ListView):
    context_object_name = 'tasks'
    model = Task
    template_name = 'issue/index.html'
    paginate_by = 3
    paginate_orphans = 1


class TaskView(DetailView):
    context_object_name = 'task'
    model = Task
    template_name = 'issue/task.html'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'issue/create.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskUpdateView(UpdateView):
    form_class = TaskForm
    template_name = 'issue/update.html'
    model = Task
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskDeleteView(DeleteView):
    template_name = 'issue/delete.html'
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('index')

