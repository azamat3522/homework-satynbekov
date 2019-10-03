from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView


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

