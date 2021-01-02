from django.shortcuts import render
from django.views.generic import ListView

from main.models import Subject


class IndexView(ListView):
    """
    View that serves the index
    :model:Subject
    :template_path:home/index.html
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


# Custom Error Views

def view400(request, *args, **kwargs):
    return render(request,
                  template_name='errors/error.html',
                  context={'error_code': "400",
                           'error_msg': "Watch what you ask for! Don't talk ĴeßʁɫŞĦ  to me!"},
                  status=400)


def view403(request, *args, **kwargs):
    return render(request,
                  template_name='errors/error.html',
                  context={'error_code': "403",
                           'error_msg': "Seems like outta your reach sweetie😎!"},
                  status=403)


def view404(request, *args, **kwargs):
    return render(request,
                  template_name='errors/error.html',
                  context={'error_code': "404", 'error_msg': "Oops!💣 You are lost! Actually how'd you end up here?🤔"},
                  status=404)


def view500(request):
    return render(request,
                  template_name='errors/error.html',
                  context={'error_code': "500", 'error_msg': "Sorry, had a party last Nyt🌃, I am so fucked 🆙."},
                  status=500)
