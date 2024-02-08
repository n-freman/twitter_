from django.test import TestCase

from blogposts.models import Blog
from users.models import CustomUser


class BlogTestCase(TestCase):
    '''
    Class for testing Blog model
    '''

    def tearDown(self):
        CustomUser.objects.all().delete()
        Blog.objects.all().delete()

    def test_blog_created_on_user_create(self):
        '''
        Tests if blog object is created when
        user is created.
        '''
        new_user = CustomUser.objects.create_user(
            'ivan@gmail.com',
            'ivanov_ivan',
            'hardPassword123!'
        )
        self.assertTrue(Blog.objects.count() == 1)

    def test_user_has_blog(self):
        new_user = CustomUser.objects.create_user(
            'ivan@gmail.com',
            'ivanov_ivan',
            'hardPassword123!'
        )
        self.assertTrue(hasattr(new_user, 'blog'))

