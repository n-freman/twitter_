from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class Blog(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        unique=True
    )


class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=140)
    creation_date = models.DateTimeField(
        auto_now_add=True
    )
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='posts'
    )

