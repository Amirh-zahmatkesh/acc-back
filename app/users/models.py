import uuid
import os

from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils.translation import gettext_lazy as _


def profile_image_file_path(instance, filename):
    """Generate file path for new profile image keeping it's extention"""
    extention = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{extention}'

    return os.path.join('uploads/profileimages/', filename)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError(_("Users must have an email address"))
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(PermissionsMixin, AbstractBaseUser):
    """Custom user model"""
    email = models.EmailField(verbose_name='ایمیل',
                              max_length=255, unique=True)
    phone_number = models.CharField(verbose_name='شماره تلفن همراه',
                                    max_length=15, blank=True)
    first_name = models.CharField(verbose_name='نام', max_length=55,
                                  blank=True)
    last_name = models.CharField(verbose_name='نام خانوادگی', max_length=55,
                                 blank=True)
    credit = models.IntegerField(verbose_name='اعتبار', null=True)
    points = models.IntegerField(verbose_name='امتیاز', null=True)
    image = models.ImageField(verbose_name='تصویر کاربری', null=True,
                              upload_to=profile_image_file_path)
    # videos = models.ManyToManyField('Video')
    is_active = models.BooleanField(verbose_name='فعال است', default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
