import string
from random import choice

from django.utils.text import slugify


def _random_str_generator(size=10, chars=string.ascii_lowercase + string.digits):
    """
    If generated slug already exists, then generates a random str to make it unique
    :param size:
    :param chars:
    :return:
    """
    return ''.join(choice(chars) for _ in range(size))


def slug_generator(instance, new_slug=None):
    """
    This generates unique value for slug field recursively.

    :param instance: model instance to generate the slug
    :param new_slug: used for recursion
    :return slug : generated unique slug
    """

    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    instance_class = instance.__class__
    queryset_exists = instance_class.objects.filter(slug=slug).exists()

    if queryset_exists:
        new_slug = f"{slug}-{_random_str_generator(size=4)}"
        return slug_generator(instance=instance, new_slug=new_slug)

    return slug
