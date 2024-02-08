from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory

from interactions.models import Follow
from interactions.views import FollowViewSet

User = get_user_model()


class FollowViewSetTestCase(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(
            username='ivan_ivanov',
            email='ivan@gmail.com',
            password='password123'
        )
        self.user2 = User.objects.create(       
            username='ivan_ivanov1',
            email='ivan1@gmail.com',
            password='password123'
        )
        self.follow_data = {
            'follower': self.user1.id,
            'blog': self.user2.blog.id
        }
        self.follow_viewset = FollowViewSet.as_view

    def test_get_list(self):
        Follow.objects.create(
            follower=self.user1,
            blog=self.user2.blog
        )
        factory = APIRequestFactory()
        request = factory.get('')
        list_view = self.follow_viewset({'get': 'list'})
        response = list_view(request)
        self.assertEqual(response.status_code, 200) 

    def test_create(self):
        factory = APIRequestFactory()
        request = factory.post('', data=self.follow_data)
        list_view = self.follow_viewset({'post': 'create'})
        response = list_view(request)
        self.assertEqual(response.status_code, 201) 

