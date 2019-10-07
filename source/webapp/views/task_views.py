from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from webapp.forms import TaskForm
from webapp.models import Task
from webapp.views.base_views import UpdateView, DeleteView


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
    key = 'task'

    def get_redirect_url(self):
        redirect('task_view', pk=self.object.pk)


class TaskDeleteView(DeleteView):
    template_name = 'issue/delete.html'
    model = Task
    key = 'task'

    def get_redirect_url(self):
        return reverse('index')

