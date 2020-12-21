from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from main.models import Subject, Unit, SubUnit, Flashcard, RelatedFile


#  Sets the models to be used as a inlines
class FlashcardAdmin(admin.StackedInline):
    model = Flashcard


class SubUnitAdmin(admin.StackedInline):
    model = SubUnit


class UnitAdmin(admin.StackedInline):
    model = Unit


#  Register models
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    inlines = [UnitAdmin]

    class Meta:
        model = Subject


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    inlines = [SubUnitAdmin]

    class Meta:
        model = Unit


@admin.register(SubUnit)
class SubUnitAdmin(admin.ModelAdmin):
    inlines = [FlashcardAdmin]

    class Meta:
        model = SubUnit


admin.site.register(Flashcard, MarkdownxModelAdmin)
admin.site.register(RelatedFile)
