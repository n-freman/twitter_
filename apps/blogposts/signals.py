from blogposts.models import Blog
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver


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

