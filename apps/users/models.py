
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    objects = CustomUserManager()
    username = models.CharField('username', max_length=40, unique=True)
    email = models.EmailField('email address', unique=True)
    password = models.TextField()
    is_staff = models.BooleanField(default=False) # type: ignore
    is_active = models.BooleanField(default=False) # type: ignore
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

