from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class Blog(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        unique=True
    )

