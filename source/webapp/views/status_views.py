from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView

from webapp.forms import StatusForm
from webapp.models import Status
from webapp.views.base_views import UpdateView, DeleteView


class StatusIndexView(ListView):
    context_object_name = 'statuses'
    model = Status
    template_name = 'status/status_index.html'


class StatusCreateView(CreateView):
    model = Status
    template_name = 'status/status_create.html'
    form_class = StatusForm

    def get_success_url(self):
        return reverse('status')


class StatusUpdateView(UpdateView):
    form_class = StatusForm
    template_name = 'status/status_update.html'
    model = Status
    key = 'status'

    def get_redirect_url(self):
        return reverse('status')


class StatusDeleteView(DeleteView):
    template_name = 'status/status_delete.html'
    model = Status
    key = 'status'

    def get_redirect_url(self):
        return reverse('status')
