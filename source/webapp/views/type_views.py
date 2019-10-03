from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView

from webapp.forms import TypeForm
from webapp.models import Type


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
