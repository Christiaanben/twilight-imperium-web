from django.test import TestCase
from .models.user import User
from rest_framework.authtoken.models import Token

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
        response = self.client.post('/registration/', data=data)
        user = User.objects.get(email=data['email'])

        self.assertEquals(response.status_code, 201)
        self.assertEquals(User.objects.count(), n_users + 1)
        self.assertEquals(user.check_password(data['password']), True)

    def test_user_login(self):
        data = {
            'email': 'LoginEmail@gmail.com',
            'password': 'Loginpass123!'
        }
        response = self.client.post('/login/', data=data)
        user = User.objects.get(email=data['email'])
        token = Token.objects.get(user= user)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['key'], token.key)
