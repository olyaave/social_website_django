from django.db import models
from django.contrib.auth.models import AbstractUser

from my import settings


class User(AbstractUser):
    is_moderator = models.BooleanField()

    REQUIRED_FIELDS = ['password', 'email', 'is_moderator']


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField(blank=True, null=True)
    subscribes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="subscribers")

    def __str__(self):
        return self.user.username
