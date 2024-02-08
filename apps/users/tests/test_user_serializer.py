from django.contrib.auth import get_user_model
from django.test import TestCase
from users.serializers import UserSerializer

User = get_user_model()


class UserSerializerTestCase(TestCase):

    def setUp(self):
        self.serializer_data = {
            'username': 'ivan_ivanov',
            'email': 'ivan@gmail.com',
            'password': 'password123'
        }

    def test_create(self):
        '''
        Test create method of user serializer
        '''
        serializer = UserSerializer(data=self.serializer_data) # type: ignore
        self.assertTrue(serializer.is_valid())
        serializer.create(serializer.validated_data)
        User.objects.get(username='ivan_ivanov') # this should not raise
    
    def test_cannot_read_password(self):
        user = User.objects.create(**self.serializer_data)
        serializer = UserSerializer(instance=user)
        self.assertIs(serializer.data.get('password', None), None)

