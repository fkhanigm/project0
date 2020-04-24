from django.db import models
from django.utils import timezone
import os
from uuid import uuid4
import re

def path_and_rename(instance, filename):
    upload_to = ''
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
        
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    title_image = models.ImageField(upload_to=path_and_rename, max_length=255, null=True, blank=True)
    text = models.TextField()
    source = models.TextField(null=True)
    source_command = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title