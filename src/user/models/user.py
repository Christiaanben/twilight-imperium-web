from django.db import models
from django.contrib.auth import models as auth_models
from django.contrib.auth.hashers import make_password


class UserManager(auth_models.BaseUserManager):
    def create_user(self, email, password, **kwargs) -> "User":
        user = self.model(email=self.normalize_email(email), password=make_password(password), **kwargs)
        user.save()

        return user

    def create_super_user(self, email: str, password: str, **kwargs) -> "User":
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        user = self.create_user(email, password, **kwargs)
        user.save()
        return user


class User(auth_models.AbstractUser):

    first_name = models.CharField(verbose_name="First Name", max_length=255)
    last_name = models.CharField(verbose_name="Last Name", max_length=255)
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
