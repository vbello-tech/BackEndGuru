import random
import string

from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from ckeditor.fields import RichTextField



# Create your models here.

def code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))


class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    post_image = models.ImageField(blank=False, upload_to="Blog/")
    body = RichTextField()
    publish_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, blank=True)

    def get_detail(self):
        return reverse("blog:detail", kwargs={
            'slug': self.slug,
            'title': self.title,
        })

    def save(self, *args, **kwargs):
        # Generate a random slug if the instance is being created and slug is empty
        if not self.pk and not self.slug:
            self.slug = code()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
