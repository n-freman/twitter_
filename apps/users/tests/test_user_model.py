from django.test import TestCase
from users.models import CustomUser


class CustomUserTestCase(TestCase):

    def tearDown(self):
        CustomUser.objects.all().delete()

    def test_user_create(self):
        new_user = CustomUser.objects.create_user(
            'ivan@gmail.com',
            'ivanov_ivan',
            'hardPassword123!'
        )
        self.assertTrue(CustomUser.objects.count() == 1)
        self.assertFalse(new_user.is_active)

    def test_user_create_superuser(self):
        superuser = CustomUser.objects.create_superuser(
            'ivan@gmail.com',
            'ivanov_ivan',
            'hardPassword123!'
        )
        self.assertTrue(CustomUser.objects.count() == 1)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_active) 

