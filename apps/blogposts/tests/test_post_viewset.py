from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory

from blogposts.models import Blog, Post
from blogposts.views import PostViewSet 

User = get_user_model()


class PostViewSetTestCase(TestCase):
    
    def setUp(self):
        self.post_viewset = PostViewSet.as_view
        user = User.objects.create(
            username='ivan_ivanov',
            email='ivan@gmail.com',
            password='password123'
        )
        self.post_data = {
            'blog': user.blog.id,
            'title': 'Post Title',
            'content': 'Lorem Ipsum Dolor sit amet'
        }

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('')
        list_view = self.post_viewset({'get': 'list'})
        response = list_view(request)
        self.assertEqual(response.status_code, 200) 

    def test_get_single(self):
        factory = APIRequestFactory()
        request = factory.get('')
        post_data = self.post_data
        del post_data['blog']
        post_data['blog_id'] = 1
        post = Post.objects.create(**post_data)
        list_view = self.post_viewset({'get': 'retrieve'})
        response = list_view(request, pk=post.pk)
        self.assertEqual(response.status_code, 200) 

    def test_create(self):
        factory = APIRequestFactory()                      
        request = factory.post('', data=self.post_data)
        list_view = self.post_viewset({'post': 'create'})
        response = list_view(request)
        self.assertEqual(response.status_code, 201) 

