from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from blogposts.models import Blog
from interactions.models import Follow

User = get_user_model()


class FollowModelTestCase(TestCase):

    def setUp(self):
        user1 = User.objects.create(
            email='ivan@gmail.com',
            username='ivan',
            password='hardPwd123'
        )
        user2 = User.objects.create(
            email='ivan1@gmail.com',
            username='ivan1',
            password='hardPwd123'
        )

    def test_follow_create(self):
        user1, user2, _ = self.create_follow()

    def test_can_follow_only_once(self):
        user1, user2, follow = self.create_follow()
        with self.assertRaises(ValidationError):
            follow = Follow(
                follower=user1,
                blog=user2.blog
            )
            follow.full_clean()

    def test_can_access_followees(self):
        user1, user2, _ = self.create_follow()
        blog = user2.blog
        followed_blogs = Blog.objects.filter(
            follows__in=user1.follows.all()
        )
        self.assertIn(blog, followed_blogs)

    def test_can_access_followers(self):
        user1, user2, _ = self.create_follow()
        blog = user2.blog
        followers = User.objects.filter(
            follows__in=blog.follows.all()
        )
        self.assertIn(user1, followers)

    def create_follow(self):
        user1 = User.objects.get(username='ivan')
        user2 = User.objects.get(username='ivan1')
        follow = Follow.objects.create(
            follower=user1,
            blog=user2.blog
        )
        return (user1, user2, follow)

