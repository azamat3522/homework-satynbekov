from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

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


class TaskUpdateView(View):

    def get(self, request, *args, **kwargs):
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        form = TaskForm(data={
            'summary': task.summary,
            'description': task.description,
            'status': task.status_id,
            'type': task.type_id
        })
        return render(request, 'issue/update.html', context={
            'form': form,
            'task': task
        })

    def post(self, request, *args, **kwargs):
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.summary = form.cleaned_data['summary']
            task.description = form.cleaned_data['description']
            task.status_id = form.cleaned_data['status']
            task.type_id = form.cleaned_data['type']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'issue/update.html', context={'form': form, 'task': task})


class TaskDeleteView(View):

    def get(self, request, *args, **kwargs):
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        return render(request, 'issue/delete.html', context={'task': task})

    def post(self, request, *args, **kwargs):
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        task.delete()
        return redirect('index')
