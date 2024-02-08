from datetime import datetime

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from blogposts.models import Post, Blog

User = get_user_model()


class PostTestCase(TestCase):

    def setUp(self):
        new_user = User(
            email='ivan@gmail.com',
            username='ivan_ivanov',
            password='hardPassword123'
        ).save()

    def tearDown(self):
        User.objects.all().delete()
        Post.objects.all().delete() 

    def test_post_create(self):
        '''
        Test that post creation does not raise any errors
        '''
        new_user = User.objects.get(username='ivan_ivanov')
        new_post = Post.objects.create(
            title='Post title',
            content='Lorem Ipsum dolor sit amet',
            blog=new_user.blog
        )

    def test_post_max_length(self):
        '''
        Function to test if max length of post content
        exceeds 140chars.
        '''
        new_user = User.objects.get(username='ivan_ivanov')
        with self.assertRaises(ValidationError):
            Post.objects.create(
                title='Post title',
                content='L'*141,
                blog=new_user.blog
            )

    def test_post_creation_date(self):
        new_user = User.objects.get(username='ivan_ivanov')
        new_post = Post.objects.create(
            title='Post title',
            content='Lorem Ipsum dolor sit amet',
            blog=new_user.blog
        )
        self.assertTrue(hasattr(new_post, 'creation_date'))
        self.assertTrue(isinstance(new_post.creation_date, datetime))

