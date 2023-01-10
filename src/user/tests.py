from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token

from .models import User


class ViewTests(TestCase):
    fixtures = ['user.yaml']

    def test_user_create(self):
        # Setup
        data = {
            'email': 'Test_email@gmail.com',
            'password': 'TestPass123!',
            'display_name': 'TestName',
        }
        n_users = User.objects.count()

        # Execute
        response = self.client.post(reverse('rest_register'), data=data)

        # Assert
        user = User.objects.get(email=data['email'])
        self.assertEquals(response.status_code, 201)
        self.assertEquals(User.objects.count(), n_users + 1)
        self.assertEquals(user.check_password(data['password']), True)

    def test_user_login(self):
        # Setup
        data = {
            'email': 'LoginEmail@gmail.com',
            'password': 'Loginpass123!'
        }

        # Execute
        response = self.client.post(reverse('rest_login'), data=data)

        # Assert
        user = User.objects.get(email=data['email'])
        token = Token.objects.get(user=user)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['key'], token.key)
