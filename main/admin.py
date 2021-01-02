from django.contrib import admin
from django.db import models
from markdownx.widgets import AdminMarkdownxWidget

from main.models import Subject, Unit, SubUnit, Flashcard, RelatedFile


#  Sets the models to be used as a inlines
class RelatedFileAdmin(admin.TabularInline):
    model = RelatedFile


class FlashcardAdmin(admin.StackedInline):
    model = Flashcard
    exclude = ['slug', ]


class SubUnitAdmin(admin.StackedInline):
    model = SubUnit
    exclude = ['slug', ]


class UnitAdmin(admin.StackedInline):
    model = Unit
    exclude = ['slug', ]


#  Register models
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    inlines = [UnitAdmin]
    search_fields = ("title__icontains",)
    fieldsets = (
        (None, {
            'fields': ("title", "image",)
        },),
    )

    class Meta:
        model = Subject

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["title"].label = "Subject Name:"
        form.base_fields["image"].label = "Subject Identifier Image(Required):"

        return form


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    inlines = [SubUnitAdmin]
    list_display = ("title", "desc", "subject")
    list_filter = ("subject",)
    search_fields = ("title__icontains",)
    fieldsets = (
        (None, {
            'fields': ("title", "desc", "image",)
        },),
    )

    class Meta:
        model = Unit

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["title"].label = "Unit Name:"
        form.base_fields["image"].label = "Unit Identifier Image(Required):"
        form.base_fields["desc"].label = "Short description:"
        return form


@admin.register(SubUnit)
class SubUnitAdmin(admin.ModelAdmin):
    inlines = [FlashcardAdmin]
    list_display = ("title", "desc", "unit")
    list_filter = ("unit",)
    search_fields = ("title__icontains",)
    fieldsets = (
        (None, {
            'fields': ("title", "desc", "image",)
        },),
    )

    class Meta:
        model = SubUnit

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["title"].label = "Subunit Name:"
        form.base_fields["image"].label = "Subunit Identifier Image(Required):"
        form.base_fields["desc"].label = "Short description:"
        return form


@admin.register(Flashcard)
class FlashcardModelAdmin(admin.ModelAdmin):
    list_filter = ("subunit",)
    search_fields = ("title__icontains",)
    fieldsets = (
        (None, {
            'fields': ("title", "image",)
        },),
        ("Content", {
            'fields': ("content_brief", "content_summary", "cheat_sheet",)
        },),
        ("Appendix", {
            'fields': ("related_file", "prerequisites",)
        },),
    )
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget}
    }

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["title"].label = "Digi Card Topic:"
        form.base_fields["image"].label = "Digi Card Identifier Image(Required):"
        form.base_fields["content_brief"].label = "Digi Card Body(Markdown styled):"
        form.base_fields["content_summary"].label = "Digi Card Summary(Markdown styled):"
        form.base_fields["cheat_sheet"].label = "Quick cheat sheets for memorization(Markdown styled):"
        form.base_fields["prerequisites"].label = "Prerequisites(Relevant subunits):"
        form.base_fields["related_file"].label = "Additional related files(Any type accepted):"

        return form


@admin.register(RelatedFile)
class RelatedFileAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ("title", "file",)
    search_fields = ("title__icontains",)

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["title"] = "File Name(with or without extension):"
        form.base_fields["file"] = "Choose from your system:"

    class Meta:
        model = RelatedFile
