from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory

from blogposts.models import Post
from interactions.models import PostRead
from interactions.views import PostReadViewSet

User = get_user_model()


class PostReadViewSetTestCase(TestCase):

    def setUp(self):
        user1 = User.objects.create(
            username='ivan_ivanov',
            email='ivan@gmail.com',
            password='password123'
        )
        user2 = User.objects.create(       
            username='ivan_ivanov1',
            email='ivan1@gmail.com',
            password='password123'
        )
        post = Post.objects.create(
            title='New Post',
            content='Lorem Ipsum dolor sit amet',
            blog=user2.blog
        )
        self.post_read_data = {
            'user': user1.id,
            'post': post.id
        }
        self.post_read_viewset = PostReadViewSet.as_view

    def test_get_list(self):
        factory = APIRequestFactory()                         
        request = factory.get('')
        list_view = self.post_read_viewset({'get': 'list'})
        response = list_view(request)
        self.assertEqual(response.status_code, 200) 

    def test_create(self):
        factory = APIRequestFactory()                         
        request = factory.post('', data=self.post_read_data)
        list_view = self.post_read_viewset({'post': 'create'})
        response = list_view(request)
        self.assertEqual(response.status_code, 201) 

