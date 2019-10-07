from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView, View



class DetailView(TemplateView):
    context_key = 'objects'
    model = None
    object_pk = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object_pk = kwargs.get('pk')
        context[self.context_key] = get_object_or_404(self.get_objects(), pk=self.object_pk)
        return context

    def get_objects(self):
        return self.model.objects.all()


class UpdateView(View):
    form_class = None
    template_name = None
    model = None
    redirect_url = ''
    key_kwarg = 'pk'
    key = 'objects'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get(self.key_kwarg)
        obj = get_object_or_404(self.model, pk=pk)

        form = self.form_class(instance=obj)
        return render(request, self.template_name, context={'form': form, self.key: obj})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get(self.key_kwarg)
        obj = get_object_or_404(self.model, pk=pk)
        form = self.form_class(instance=obj, data=request.POST)
        if form.is_valid():
            self.object = form.save()
            return redirect(self.get_redirect_url())
        else:
            return render(self.request, self.template_name, context={'form': form})

    def get_redirect_url(self):
        return self.redirect_url


class DeleteView(View):
    template_name = None
    model = None
    key_kwarg = 'pk'
    key = 'object'
    redirect_url = ''

    def get(self, request, *args, **kwargs):
        pk = kwargs.get(self.key_kwarg)
        obj = get_object_or_404(self.model, pk=pk)
        return render(request, self.template_name, context={self.key: obj})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get(self.key_kwarg)
        obj = get_object_or_404(self.model, pk=pk)
        try:
            self.object = obj.delete()
            return redirect(self.get_redirect_url())
        except:
            raise Exception('Can not be deleted')


    def get_redirect_url(self):
        return self.redirect_url
