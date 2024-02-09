from blogposts.models import Post
from blogposts.views import PostFeedView
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from interactions.models import Follow

from blogposts.serializers import PostSerializer

User = get_user_model()


class PostsFeedView(TestCase):

    def setUp(self):
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
        self.posts = list(
            map(
                lambda item: PostSerializer(instance=item).data,
                self.posts
            )
        )

    def test_get_feed(self):
        factory = APIRequestFactory()
        request = factory.get('')
        view = PostFeedView.as_view()
        response = view(request, 1)
        self.assertEqual(response.status_code, 200)

