from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import TaskForm, SimpleSearchForm
from webapp.models import Task, Project
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class IndexView(ListView):
    context_object_name = 'tasks'
    model = Task
    template_name = 'issue/index.html'
    paginate_by = 3
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_query = self.get_search_query()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        if self.search_query:
            context['query'] = urlencode({'search': self.search_query})
        context['form'] = self.form
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_query:
            queryset = queryset.filter(
                Q(summary__icontains=self.search_query)
                | Q(description__icontains=self.search_query)
            )
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_query(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class TaskView(DetailView):
    context_object_name = 'task'
    model = Task
    template_name = 'issue/task.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'issue/create.html'
    form_class = TaskForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['project'] = Project.objects.filter(project_users__user=self.request.user)
        return kwargs

    def get_project(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Project, pk=pk)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.project = self.get_project()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:task_view', kwargs={'pk': self.object.pk})


class TaskUpdateView(UserPassesTestMixin, UpdateView):
    form_class = TaskForm
    template_name = 'issue/update.html'
    model = Task
    context_object_name = 'task'

    def test_func(self):
        obj = self.get_object()
        return obj.project.project_users.filter(user=self.request.user)

    def get_success_url(self):
        return reverse('webapp:task_view', kwargs={'pk': self.object.pk})


class TaskDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'issue/delete.html'
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('webapp:index')

    def test_func(self):
        obj = self.get_object()
        return obj.project.project_users.filter(user=self.request.user)

