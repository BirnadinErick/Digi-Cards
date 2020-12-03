from django.views.generic import ListView

from main.models import Subject


class IndexView(ListView):
    """
    View that serves the index
    TODO: Add a feature to render no of units in subject
    """

    template_name = 'home/index_final.html'  # template to render
    context_object_name = 'subjects'  # output object
    model = Subject

    def get_queryset(self):
        return Subject.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['css_color'] = ['transparent-blue-text',
                                'fast-green-text',
                                'transparent-green-text',
                                'fast-pink-text-dark',
                                'fast-pink-text',
                                ]
        return context
