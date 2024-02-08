from rest_framework import viewsets

from interactions.serializers import PostReadSerializer, FollowSerializer
from interactions.models import PostRead, Follow


class PostReadViewSet(viewsets.ModelViewSet):
    queryset = PostRead.objects.all()
    serializer_class = PostReadSerializer


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

