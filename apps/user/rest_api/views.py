from rest_framework import viewsets

from apps.user.models import User
from apps.user.rest_api.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
