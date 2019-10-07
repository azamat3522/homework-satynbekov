from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView

from webapp.forms import StatusForm
from webapp.models import Status


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
