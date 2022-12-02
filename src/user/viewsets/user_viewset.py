from rest_framework import viewsets, permissions
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
# from user.serializer import UserSerializer
from user.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
