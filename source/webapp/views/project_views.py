from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProjectTaskForm, ProjectForm, SimpleSearchForm
from webapp.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin

class ProjectIndexView(ListView):
    context_object_name = 'projects'
    model = Project
    template_name = 'project/project_index.html'
    ordering = ['created_at']
    paginate_by = 3
    paginate_orphans = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = SimpleSearchForm()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = SimpleSearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data['search']
            if query:
                queryset = queryset.filter(name__icontains=query)
        return queryset



class ProjectView(DetailView):
    template_name = 'project/project.html'
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProjectTaskForm()
        tasks = context['project'].tasks.order_by('-created_at')
        self.paginate_tasks_to_context(tasks, context)
        return context

    def paginate_tasks_to_context(self, tasks, context):
        paginator = Paginator(tasks, 3, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['tasks'] = page.object_list
        context['is_paginated'] = page.has_other_pages()


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'project/project_create.html'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'project/project_update.html'
    context_object_name = 'project'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'project/project_delete.html'
    context_object_name = 'project'
    success_url = reverse_lazy('project')

