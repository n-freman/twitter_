from blogposts.models import Blog
from blogposts.views import BlogViewSet
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIRequestFactory

User = get_user_model()


class BlogViewSetTestCase(TestCase):
    
    def setUp(self):
        self.blog_viewset = BlogViewSet.as_view

    def test_get_list(self):
        factory = APIRequestFactory()                  
        request = factory.get('')
        user = User.objects.create( # this automatically creates blog object
            username='ivan_ivanov',
            email='ivan@gmail.com',
            password='password123'
        )
        list_view = self.blog_viewset({'get': 'list'})
        response = list_view(request)
        self.assertEqual(response.status_code, 200) 


    def test_get_single(self):
        factory = APIRequestFactory()                  
        request = factory.get('')
        user = User.objects.create( # this automatically creates blog object
            username='ivan_ivanov',
            email='ivan@gmail.com',
            password='password123'
        )
        list_view = self.blog_viewset({'get': 'retrieve'})
        response = list_view(request, pk=user.blog.pk)
        self.assertEqual(response.status_code, 200) 

