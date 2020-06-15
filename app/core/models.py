import uuid
import os

from django.conf import settings
from django.db import models


def certificate_image_file_path(instance, filename):
    """Generate file path for new certificate image keeping it's extention"""
    extention = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{extention}'

    return os.path.join('uploads/certificateimages/', filename)


class Certificate(models.Model):
    """Certificates for users who passed specific tests"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='certificates',
                             on_delete=models.CASCADE, null=True)
    name = models.CharField(verbose_name='نام', max_length=255)
    slug = models.SlugField()
    image = models.ImageField(null=True, upload_to=certificate_image_file_path)
    thumbnail = models.ImageField(null=True,
                                  upload_to=certificate_image_file_path)
    grade = models.IntegerField(verbose_name='نمره', null=True)
    minimum_grade = models.IntegerField(verbose_name='حداقل نمره')

    def __str__(self):
        return self.name


class Category(models.Model):
    """Category for posts, videos ..."""
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, on_delete=models.SET_NULL,
                               null=True, related_name='children')

    class Meta:
        unique_together = ('slug', 'parent', )
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])


class Keyword(models.Model):
    """A model for storing keywords for SEO"""
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word


class Faq(models.Model):
    """A model for the FAQ"""
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f'q: {self.question} a: {self.answer}'
