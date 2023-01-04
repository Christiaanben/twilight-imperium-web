from django.test import TestCase
from .models.user import User


class ViewTests(TestCase):

    def test_user_create(self):
        # Setup
        data = {
            'email': 'Test_email@gmail.com',
            'password1': 'TestPass123!',
            'password2': 'TestPass123!',
            'display_name': 'TestName',
        }
        n_users = User.objects.count()
        # Execute
        response = self.client.post('/registration/', data=data)
        # Assert
        user = User.objects.get(email=data['email'])

        self.assertEquals(response.status_code, 201)
        self.assertEquals(User.objects.count(), n_users + 1)
        self.assertEquals(user.check_password(data['password1']), True)
