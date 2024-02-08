from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from blogposts.models import Blog

User = get_user_model()


class BlogTestCase(TestCase):
    '''
    Class for testing Blog model
    '''

    def setUp(self):
        new_user = User.objects.create_user(
            'ivan@gmail.com',
            'ivanov_ivan',
            'hardPassword123!'
        )

    def tearDown(self):
        User.objects.all().delete()
        Blog.objects.all().delete()

    def test_blog_created_on_user_create(self):
        '''
        Tests if blog object is created when
        user is created.
        '''
        new_user = User.objects.get(username='ivanov_ivan')
        self.assertTrue(Blog.objects.count() == 1)

    def test_user_has_blog(self):
        new_user = User.objects.get(username='ivanov_ivan')
        self.assertTrue(hasattr(new_user, 'blog'))

    def test_user_can_have_one_blog(self):
        new_user = User.objects.get(username='ivanov_ivan')
        with self.assertRaises(ValidationError):
            # This should raise as blog was already automatically
            # created for this user
            Blog(user=new_user).full_clean()

