from datetime import datetime

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

from webapp.forms import ProjectTaskForm, ProjectForm, SimpleSearchForm, TeamUpdateForm
from webapp.models import Project, Team
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


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


class ProjectCreateView(PermissionRequiredMixin, CreateView):
    model = Project
    template_name = 'project/project_create.html'
    form_class = ProjectForm
    permission_required = 'webapp.add_project'
    permission_denied_message = "Доступ запрещён"

    def form_valid(self, form):
        users = form.cleaned_data.pop('user')
        users_list = list(users)
        users_list.append(self.request.user)
        self.object = form.save()
        for user in users_list:
            Team.objects.create(user=user, project=self.object, start_date=datetime.now())
        return redirect(self.get_success_url())

    # def get_user(self):
    #     project = self.object
    #     user = self.request.user
    #     return Team.objects.create(project=project, user=user, start_date=datetime.now())

    def get_success_url(self):
        # self.get_user()
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})


class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'project/project_update.html'
    context_object_name = 'project'
    form_class = ProjectForm
    permission_required = 'webapp.change_project'
    permission_denied_message = "Доступ запрещён"
    # fields = ['name', 'description']


    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    model = Project
    template_name = 'project/project_delete.html'
    context_object_name = 'project'
    success_url = reverse_lazy('webapp:project')
    permission_required = 'webapp.delete_project'
    permission_denied_message = "Доступ запрещён"


class ProjectUsersUpdateView(PermissionRequiredMixin, FormView):
    template_name = 'project/change_project_members.html'
    form_class = TeamUpdateForm
    permission_required = 'webapp.change_team'
    permission_denied_message = "Доступ запрещён"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = get_object_or_404(Project, pk=self.kwargs['pk'])
        return context

    def get_initial(self):
        initial = super().get_initial()
        self.project = get_object_or_404(Project, pk=self.kwargs['pk'])
        initial['team'] = User.objects.filter(user_projects__project=self.project, user_projects__end_date=None)
        return initial

    def form_valid(self, form):
        self.project = get_object_or_404(Project, pk=self.kwargs['pk'])
        cleaned_users = form.cleaned_data.pop('team_users')
        # print(cleaned_users)
        initial_users = form.initial.get('team')
        # print(initial_users)

        team = Team.objects.filter(project=self.project)

        for user in team:
            user.end_date = datetime.now()
            user.save()

        for user in cleaned_users:
            Team.objects.create(user=user, project=self.project, start_date=datetime.now())

        # for user in cleaned_users:
        #     if not user in initial_users:
        #         Team.objects.create(user=user, project=self.project, start_date=datetime.now())



        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.project.pk})

