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
    class Meta:
        model = User
        fields = ['email', 'password', 'display_name']

    username = None
    display_name = serializers.CharField(max_length= 30,
                                         min_length= 3,
                                         required= True,)
    password = serializers.CharField(write_only= True, required= True)
    password1 = serializers.CharField(write_only= True, required= False)
    password2 = serializers.CharField(write_only= True, required= False)


    @transaction.atomic
    def validate(self, data):
        data['password1'] = data['password']
        data['password2'] = data['password']
        return data

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.display_name = self.data.get('display_name')
        user.save()
        return user

