from django.urls import path

from main.views import *

app_name = 'main'

urlpatterns = [
    path('subject/<slug:subject_slug>/', SubjectView.as_view(), name='subject'),  # Subject view called from IndexView
    path('unit/<slug:unit_slug>/', UnitView.as_view(), name='unit'),  # UnitView view called from SubjectView
    path('subunit/<slug:subunit_slug>', SubUnitView.as_view(), name='subunit'),  # SubUnitView view called from UnitView
    path('card/<slug:slug>', FlashcardView.as_view(), name='flashcard'),  # Flashcard view called from SubUnitView
]
