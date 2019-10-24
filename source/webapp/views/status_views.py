from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from webapp.forms import StatusForm
from webapp.models import Status
from django.contrib.auth.mixins import LoginRequiredMixin


class StatusIndexView(ListView):
    context_object_name = 'statuses'
    model = Status
    template_name = 'status/status_index.html'


class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    template_name = 'status/status_create.html'
    form_class = StatusForm

    def get_success_url(self):
        return reverse('status')


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    form_class = StatusForm
    template_name = 'status/status_update.html'
    model = Status
    context_object_name = 'status'

    def get_success_url(self):
        return reverse('status')


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'status/status_delete.html'
    model = Status
    context_object_name = 'status'
    success_url = reverse_lazy('status')