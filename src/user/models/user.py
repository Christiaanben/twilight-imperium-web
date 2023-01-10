from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs) -> "User":
        user = self.model(email=self.normalize_email(email), password=make_password(password), **kwargs)
        user.save()

        return user

    def create_superuser(self, email: str, password: str, **kwargs) -> "User":
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        user = self.create_user(email, password, **kwargs)
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    display_name = models.CharField(max_length=30)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
