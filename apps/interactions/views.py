from interactions.models import Follow, PostRead
from interactions.serializers import FollowSerializer, PostReadSerializer
from rest_framework import viewsets


class PostReadViewSet(viewsets.ModelViewSet):
    queryset = PostRead.objects.all()
    serializer_class = PostReadSerializer


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

