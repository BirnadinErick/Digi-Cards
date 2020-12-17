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
    desc = models.CharField(max_length=100, blank=False, default="Description for the unit goes here!")

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
    desc = models.CharField(max_length=100, blank=False, default="Description for the subunit goes here!")

    def __str__(self):
        return self.title


class Flashcard(models.Model):
    """
    Model for each flashcard
    """

    slug = models.SlugField(null=True, blank=True)
    subunit = models.ForeignKey(SubUnit, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    last_updated = models.DateField()
    content_brief = MarkdownxField()
    content_summary = MarkdownxField()
    cheat_sheet = MarkdownxField()
    image = ProcessedImageField(upload_to='background_img/card/',
                                processors=[ImageResize()],
                                format='JPEG',
                                options={'quality': 30})

    def __str__(self):
        return self.title


# ------------------------------------- UTILITY AREA ----------------------------------------------------

# Func. to append slug to the model field
def slug_appender(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slug_generator(instance)


# Signal manager to trigger slug generation
pre_save.connect(slug_appender, sender=Subject)
pre_save.connect(slug_appender, sender=Unit)
pre_save.connect(slug_appender, sender=SubUnit)
pre_save.connect(slug_appender, sender=Flashcard)
