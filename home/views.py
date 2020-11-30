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
