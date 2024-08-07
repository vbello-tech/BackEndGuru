import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.shortcuts import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist


class CustomUserManager(BaseUserManager):

    def create_user(self, email, username, password, **extra_fields):
        """
          Create and save a SuperUser with the given email,first name , lastname and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        if not username:
            raise ValueError(_('Username must be set'))
        if not password:
            raise ValueError(_('Password must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given email,first name , lastname and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, username, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, unique=True, verbose_name='email address')
    password = models.CharField(max_length=200)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    # required for creating user
    REQUIRED_FIELDS = ['username', ]

    class Meta:
        ordering = ['-date_joined']
        verbose_name_plural = "Custom Users"

    def __str__(self):
        return f'{self.username}'


class UserProfile(models.Model):
    """
    model for user profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="Profile/", blank=True, null=True)
    stack = models.CharField(max_length=20, blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    other = models.URLField(blank=True, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def get_profile(self):
        """
        redirect to profile view page when function is called
        """
        return reverse("user:profile")

    def __str__(self):
        return self.user


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def user_profile(sender, instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, created, *args, **kwargs):
    try:
        instance.userprofile.save()
    except ObjectDoesNotExist:
        UserProfile.objects.create(user=instance)
