import random
import string
import uuid

from django.db import models
from django.conf import settings
from django.urls import reverse

Difficulty = [
    ('NEWBIE', 'NEWBIE'),
    ('JUNIOR', 'JUNIOR'),
    ('INTERMEDIATE', 'INTERMEDIATE'),
    ('ADVANCED', 'ADVANCED'),
    ('GURU', 'GURU'),
]


def code():
    random_code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return random_code


class Challenge(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    features = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="Challenge/", blank=True, null=True)
    difficulty = models.CharField(max_length=15, choices=Difficulty, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.title

    def get_detail(self):
        return reverse("challenge:detail", kwargs={
            'id': self.id,
            'title': self.title,
        })


class ChallengeEntry(models.Model):
    participant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, related_name="entry_task", on_delete=models.CASCADE)
    description = models.CharField(max_length=150, blank=True, null=True)
    schema_image = models.ImageField(upload_to="Challenge/", blank=True, null=True)
    language = models.CharField(max_length=150, blank=True, null=True)
    framework = models.CharField(max_length=150, blank=True, null=True)
    database = models.CharField(max_length=150, blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    project = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    completed = models.BooleanField(default=False)
    datesubmitted = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Generate a random slug if the instance is being created and slug is empty
        if not self.pk and not self.slug:
            self.slug = code()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.participant} entry for {self.challenge.title}"

    def get_entry(self):
        return reverse("challenge:entry_detail", kwargs={
            'slug': self.slug,
        })

    def submit_entry(self):
        return reverse("challenge:submit_entry", kwargs={
            'slug': self.slug,
        })
