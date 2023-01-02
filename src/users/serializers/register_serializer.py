from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

RegisterSerializer
class CustomRegisterSerializer(RegisterSerializer):
    username = None
    display_name = serializers.CharField(max_length=30,
                                         min_length=3,
                                         required=True,)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'display_name']

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        print("Display name data: " + str(self.data.get('display_name')))
        user.display_name = self.data.get('display_name')
        user.save()
        return user

