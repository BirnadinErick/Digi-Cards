from PIL import Image
from django.db import models
from django.db.models.signals import pre_save
from imagekit.models import ProcessedImageField
from markdownx.models import MarkdownxField

from main.utils import slug_generator


# Helper Class to preprocess images
class ImageResize(object):
    def process(self, image):
        width, height = image.size
        gcd = self._aspect_ratio(width, height)
        if width // gcd == 16 and (height // gcd == 9 or height // gcd == 10):
            return image.resize((1920, 1080), Image.ANTIALIAS)
        else:
            return image

    def _aspect_ratio(self, w, h):
        if h == 0:
            return w
        return self._aspect_ratio(h, w % h)


class Subject(models.Model):
    """
        Model for each Subject
    """

    slug = models.SlugField(null=True, blank=True)
    title = models.CharField(max_length=50, unique=True)
    image = ProcessedImageField(upload_to='background_img/subject/',
                                processors=[ImageResize()],
                                format='JPEG',
                                options={'quality': 30})

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title


class Unit(models.Model):
    """
        Model for each Unit
    """

    slug = models.SlugField(null=True, blank=True)
    title = models.CharField(max_length=255, unique=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    image = ProcessedImageField(upload_to='background_img/unit/',
                                processors=[ImageResize()],
                                format='JPEG',
                                options={'quality': 30})
    desc = models.CharField(max_length=100, blank=False, default="Description for the unit goes here!",
                            verbose_name="Description")

    class Meta:
        ordering = ("subject", "title")

    def __str__(self):
        return self.title


class SubUnit(models.Model):
    """
        Model for each Subunit
    """

    slug = models.SlugField(null=True, blank=True)
    title = models.CharField(max_length=255)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    image = ProcessedImageField(upload_to='background_img/subunit/',
                                processors=[ImageResize()],
                                format='JPEG',
                                options={'quality': 30})
    desc = models.CharField(max_length=100, blank=False, default="Description for the subunit goes here!",
                            verbose_name="Description")

    class Meta:
        ordering = ("unit", "title")

    def __str__(self):
        return self.title


class RelatedFile(models.Model):
    """
    Model for related file for each flashcard
    """

    slug = models.SlugField(null=True, blank=True)
    title = models.CharField(max_length=100, blank=False)
    file = models.FileField(upload_to="related_files/", blank=False)

    def __str__(self):
        return self.title


class Flashcard(models.Model):
    """
    Model for each flashcard
    """

    slug = models.SlugField(null=True, blank=True)
    subunit = models.ForeignKey(SubUnit, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    last_updated = models.DateField(blank=True)
    content_brief = MarkdownxField()
    content_summary = MarkdownxField()
    cheat_sheet = MarkdownxField()
    prerequisites = models.ManyToManyField(SubUnit, related_name="requirements", blank=True)
    image = ProcessedImageField(upload_to='background_img/card/',
                                processors=[ImageResize()],
                                format='JPEG',
                                options={'quality': 30})
    related_file = models.ManyToManyField(RelatedFile, blank=True)

    class Meta:
        ordering = ("subunit", "last_updated", "title")

    def __str__(self):
        return self.title

    @property
    def change_url(self):
        return f"/guardian/main/flashcard/{self.id}/change/"


# ------------------------------------- UTILITY AREA ----------------------------------------------------

# Func. to append slug to the model field
def slug_appender(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slug_generator(instance)


# Func. to update the last_updated field of a digi-card
def last_update_check(sender, instance, *args, **kwargs):
    import datetime
    now = datetime.datetime.now()
    instance.last_updated = now


# Signal manager to trigger slug generation
pre_save.connect(slug_appender, sender=Subject)
pre_save.connect(slug_appender, sender=Unit)
pre_save.connect(slug_appender, sender=SubUnit)
pre_save.connect(slug_appender, sender=Flashcard)
pre_save.connect(last_update_check, sender=Flashcard)
