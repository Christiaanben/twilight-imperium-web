from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    display_name = models.CharField(max_length=30)
    REQUIRED_FIELDS = []
