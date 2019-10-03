from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView
from django.http import Http404

# from webapp.forms import TaskForm
from webapp.forms import TaskForm, StatusForm, TypeForm
from webapp.models import Task, Status, Type


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



class StatusIndexView(TemplateView):
    template_name = 'status/status_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        return context


class StatusCreateView(View):
    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, 'status/status_create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            Status.objects.create(
                name=form.cleaned_data['name']
            )
            return redirect('status')
        else:
            return render(request, 'status/status_create.html', context={'form': form})

class StatusUpdateView(View):
    def get(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        form = StatusForm(data={
            'name': status.name
        })
        return render(request, 'status/status_update.html', context={
            'form': form,
            'status': status
        })
    def post(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status.name = form.cleaned_data['name']
            status.save()
            return redirect('status')
        else:
            return render(request, 'status/status_update.html', context={'form': form, 'status': status})



class StatusDeleteView(View):

    def get(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        return render(request, 'status/status_delete.html', context={'status': status})

    def post(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        try:
            status.delete()
            return redirect('status')
        except:
            raise Exception('Cannot delete status')



class TypeIndexView(TemplateView):
    template_name = 'type/type_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        return context


class TypeCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TypeForm()
        return render(request, 'type/type_create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            Type.objects.create(
                name=form.cleaned_data['name']
            )
            return redirect('type')
        else:
            return render(request, 'type/type_create.html', context={'form': form})


class TypeUpdateView(View):
    def get(self, request, *args, **kwargs):
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        form = TypeForm(data={
            'name': type.name
        })
        return render(request, 'type/type_update.html', context={
            'form': form,
            'type': type
        })
    def post(self, request, *args, **kwargs):
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type.name = form.cleaned_data['name']
            type.save()
            return redirect('type')
        else:
            return render(request, 'type/type_update.html', context={'form': form, 'type': type})



class TypeDeleteView(View):

    def get(self, request, *args, **kwargs):
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        return render(request, 'type/type_delete.html', context={'type': type})

    def post(self, request, *args, **kwargs):
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        try:
            type.delete()
            return redirect('type')
        except:
            raise Exception('Cannot delete type')
