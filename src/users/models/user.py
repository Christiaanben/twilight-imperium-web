from django.contrib.auth import models as auth_models

class User(auth_models.AbstractUser):
    display_name = auth_models.models.CharField(max_length=30)
    REQUIRED_FIELDS = []
