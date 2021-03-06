from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from webapp.forms import TypeForm
from webapp.models import Type
from django.contrib.auth.mixins import LoginRequiredMixin


class TypeIndexView(ListView):
    context_object_name = 'types'
    model = Type
    template_name = 'type/type_index.html'


class TypeCreateView(LoginRequiredMixin, CreateView):
    model = Type
    template_name = 'type/type_create.html'
    form_class = TypeForm

    def get_success_url(self):
        return reverse('webapp:type')


class TypeUpdateView(LoginRequiredMixin, UpdateView):
    form_class = TypeForm
    template_name = 'type/type_update.html'
    model = Type
    context_object_name = 'type'

    def get_success_url(self):
        return reverse('webapp:type')


class TypeDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'type/type_delete.html'
    model = Type
    context_object_name = 'type'
    success_url = reverse_lazy('webapp:type')


