import random
import string

from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse


# Create your models here.

def code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))


class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    post_image = models.ImageField(blank=False, upload_to="Blog/")
    body = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(default=code())

    def get_detail(self):
        return reverse("blog:detail", kwargs={
            'slug': self.slug,
            'title': self.title,
        })

    def __str__(self):
        return self.title
