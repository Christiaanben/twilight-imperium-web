from django.db import models
from django.contrib.auth import models as auth_models
from user import User


class UserManager(auth_models.BaseUserManager):

    def create_user(self, first_name: str,
                    last_name: str,
                    email: str,
                    password: str = None,
                    is_staff=False,
                    is_superuser=False) -> "User":


        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.is_active = True
        user.save()

        return user

    def create_super_user(self, first_name: str,
                    last_name: str,
                    email: str,
                    password: str = None) -> "User":
        user = self.create_user(first_name, last_name, email, password, is_staff=True, is_superuser=True)
        user.save()
        return user
