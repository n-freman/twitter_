from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from users.views import UserViewSet

User = get_user_model()


class UserViewSetTestCase(TestCase):

    def setUp(self):
        self.user_viewset = UserViewSet.as_view
        self.user_data = {
            'username': 'ivanov_ivan',
            'email': 'ivan@gmail.com',                
            'password': 'password123'                 
        }

    def test_get_user_list(self):
        factory = APIRequestFactory()
        request = factory.get('')
        user = User.objects.create(**self.user_data)
        list_view = self.user_viewset({'get': 'list'})
        response = list_view(request)
        self.assertEqual(response.status_code, 200) 

    def test_get_single_user(self):
        factory = APIRequestFactory()
        request = factory.get('')
        user = User.objects.create(**self.user_data)
        list_view = self.user_viewset({'get': 'retrieve'})
        response = list_view(request, pk=user.pk)
        self.assertEqual(response.status_code, 200) 

    def test_create_user(self):
        factory = APIRequestFactory()
        request = factory.post('', data={**self.user_data})
        create_view = self.user_viewset({'post': 'create'})
        response = create_view(request)
        self.assertEqual(response.status_code, 201) 

