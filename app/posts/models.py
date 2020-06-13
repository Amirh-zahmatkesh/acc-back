# import uuid
# import os

# from django.conf import settings
# from django.db import models

# from ckeditor.fields import RichTextField


# def post_image_file_path(instance, filename):
#     """Generate file path for new post image keeping it's extention"""
#     extention = filename.split('.')[-1]
#     filename = f'{uuid.uuid4()}.{extention}'

#     return os.path.join('uploads/postimages/', filename)


# class Post(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
#     title = models.CharField(max_length=120)
#     description = RichTextField()
#     content = RichTextField()
#     reading_time = models.IntegerField()
#     thumbnail = models.ImageField(null=True, upload_to=post_image_file_path)
#     image = models.ImageField(null=True, upload_to=post_image_file_path)
#     likes = models.IntegerField(null=True)
#     views = models.IntegerField(null=True)
#     rate = models.DecimalField(max_digits=2, decimal_places=1, null=True)
#     category = models.ForeignKey('Category', null=True, blank=True,
#                                  on_delete=models.SET_NULL())
#     keywords = models.ForeignKey('Keyword', null=True, blank=True,
#                                  on_delete=models.SET_NULL())
#     # FAQ
#     # examples
#     # questions
#     created_on = models.DateTimeField(auto_now_add=True)
#     updated_on = models.DateTimeField(auto_now=True)
#     draft = models.BooleanField(default=True)
#     slug = models.SlugField(unique=True)

#     def __str__(self):
#         return self.title

#     def get_cat_list(self):
#         k = self.category

#         breadcrumb = ["dummy"]
#         while k is not None:
#             breadcrumb.append(k.slug)
#             k = k.parent
#         for i in range(len(breadcrumb)-1):
#             breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
#         return breadcrumb[-1:0:-1]
