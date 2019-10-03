from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView


from webapp.forms import TaskForm
from webapp.models import Task


class IndexView(TemplateView):
    template_name = 'issue/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskView(TemplateView):
    template_name = 'issue/task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_pk = kwargs.get('pk')
        context['task'] = get_object_or_404(Task, pk=task_pk)
        return context


class TaskCreateView(View):

    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'issue/create.html', context={'form': form})

    def post(self,request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type']
            )
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'issue/create.html', context={'form': form})


class TaskUpdateView(View):


    def get(self, request, *args, **kwargs):
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        form = TaskForm(data={
            'summary': task.summary,
            'description': task.description,
            'status': task.status_id,
            'type':task.type_id
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




