from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView

from webapp.forms import TypeForm
from webapp.models import Type
from webapp.views.base_views import UpdateView, DeleteView


class TypeIndexView(ListView):
    context_object_name = 'types'
    model = Type
    template_name = 'type/type_index.html'


class TypeCreateView(CreateView):
    model = Type
    template_name = 'type/type_create.html'
    form_class = TypeForm

    def get_success_url(self):
        return reverse('type')


class TypeUpdateView(UpdateView):
    form_class = TypeForm
    template_name = 'type/type_update.html'
    model = Type
    key = 'type'

    def get_redirect_url(self):
        return reverse('type')


class TypeDeleteView(DeleteView):
    template_name = 'type/type_delete.html'
    model = Type
    key = 'type'

    def get_redirect_url(self):
        return reverse('type')
