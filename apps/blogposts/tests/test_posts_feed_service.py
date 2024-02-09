from django.test import TestCase
from django.contrib.auth import get_user_model

from blogposts.models import Post
from blogposts.services import PostsFeedService
from interactions.models import Follow

User = get_user_model()


class PostsFeedServiceTestCase(TestCase):

    def setUp(self):
        self.service = PostsFeedService
        self.users = []
        for i in range(3):
            self.users.append(User.objects.create(
                username=f'ivan_ivanov{i}',
                email=f'ivan{i}@gmail.com',
                password='password123'
            ))
        Follow.objects.create(
            follower=self.users[0],
            blog=self.users[1].blog
        )
        self.posts = []
        for user in self.users[1:]:
            self.posts.append(Post.objects.create(
                title=f'Post from {user.username}',
                content='Lorem ipsum dolor sit amet',
                blog=user.blog
            ))

    def test_posts_feed_fetching(self):
        feed_posts = self.service.get_posts_feed_for_user(self.users[0].id)
        self.assertIn(self.posts[0], feed_posts)
        self.assertNotIn(self.posts[1], feed_posts)

