from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to="profile/", null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
