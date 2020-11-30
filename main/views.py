from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from main.models import *


class SubjectView(ListView):
    """
        Subject View
        Inherits ListView from Django Generic Views
        :param subject_slug :type slug
    """

    template_name = 'main/subject.html'
    context_object_name = 'units'

    def get_queryset(self):
        self.subject = get_object_or_404(Subject, slug=self.kwargs['subject_slug'])
        return Unit.objects.filter(subject=self.subject)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.subject.title
        context['subject'] = self.subject
        return context


class UnitView(ListView):
    """
        Unit View
        Inherits ListView from Django Generic Views
        :param unit_slug :type slug
    """

    template_name = 'main/unit.html'
    context_object_name = 'subunits'

    def get_queryset(self):
        self.unit = get_object_or_404(Unit, slug=self.kwargs['unit_slug'])
        return SubUnit.objects.filter(unit=self.unit)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.unit.title
        context['unit'] = self.unit
        return context


class SubUnitView(ListView):
    """
        SubUnit View
        Inherits ListView from Django Generic Views
        :param subunit_slug :type slug
    """

    template_name = 'main/subunit.html'
    context_object_name = 'flashcards'

    def get_queryset(self):
        self.subunit = get_object_or_404(SubUnit, slug=self.kwargs['subunit_slug'])
        return Flashcard.objects.filter(subunit=self.subunit)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.subunit.title
        context['subunit'] = self.subunit
        return context


class FlashcardView(DetailView):
    """
    Flashcard View
    Inherits DetailView from Django Generic Views
    :param slug :type slug
    """

    template_name = 'main/flashcard.html'
    context_object_name = 'flashcard'
    model = Flashcard

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
