from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from blogposts.models import Post
from .models import PostRead

User = get_user_model()


class PostReadsTestCase(TestCase):

    def setUp(self):
        new_user = User.objects.create(
            email='ivan@gmail.com',
            username='ivan_ivanov',
            password='password123',
        )
        new_post = Post.objects.create(
            title='New Post',
            content='Lorem Ipsum',
            blog=new_user.blog,
        )

    def test_create_post_read(self):
        user = User.objects.get(username='ivan_ivanov')
        post = Post.objects.get(title='New Post')
        PostRead.objects.create(
            post=post,
            user=user
        )

    def test_cannot_read_the_same_post_twice(self):
        user = User.objects.get(username='ivan_ivanov')
        post = Post.objects.get(title='New Post')
        PostRead.objects.create(
            post=post,
            user=user,
        )
        with self.assertRaises(ValidationError):
            PostRead.objects.create(
                post=post,
                user=user,
            )

