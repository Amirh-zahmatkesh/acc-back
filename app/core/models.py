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
    image = models.ImageField(null=True, upload_to=certificate_image_file_path)
    thumbnail = models.ImageField(null=True,
                                  upload_to=certificate_image_file_path)
    grade = models.IntegerField(verbose_name='نمره', null=True)
    minimum_grade = models.IntegerField(verbose_name='حداقل نمره')

    def __str__(self):
        return self.name
