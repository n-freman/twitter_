from blogposts.models import Blog, Post
from django.contrib.auth import get_user_model
from django.db import models


class PostRead(models.Model):
    '''
    Model representing single reading of a post
    '''
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='reads'
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='post_reads'
    )

    class Meta:
        unique_together = ('post', 'user')


class Follow(models.Model):
    '''
    Model represents following a blog
    '''
    follower = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='follows'
    )
    blog = models.ForeignKey(
        Blog,
        on_delete=models.Case,
        related_name='follows'
    )

    class Meta:
        unique_together = ('follower', 'blog')

