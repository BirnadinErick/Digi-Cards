from django.views.generic import ListView, TemplateView

from main.models import Subject


class IndexView(ListView):
    """
    View that serves the index
    TODO: Add a feature to render no of units in subject
    """

    template_name = 'home/index.html'  # template to render
    context_object_name = 'subjects'  # output object name
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


class Http400Error(TemplateView):
    template_name = 'errors/error.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['error_code'] = "404"
        context['error_msg'] = "Oops!💣 You are lost! Actually how'd you end up here?🤔"
        return context


if __name__ != "__main__":
    view404 = Http400Error.as_view()
