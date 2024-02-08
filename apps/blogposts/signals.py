from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from blogposts.models import Blog


@receiver(post_save, sender=get_user_model())
def handle_user_create(
    sender,
    signal,
    instance,
    created,
    **kwargs
):
    if not created:
        return
    Blog.objects.create(user=instance)

