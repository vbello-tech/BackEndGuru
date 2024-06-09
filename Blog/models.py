from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings


# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    post_image = models.ImageField(blank=False, upload_to="Blog/")
    body = RichTextUploadingField()
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
