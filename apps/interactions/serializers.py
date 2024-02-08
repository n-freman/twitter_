from interactions.models import Follow, PostRead
from rest_framework import serializers


class PostReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostRead
        fields = ['id', 'post', 'user']


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = ['id', 'follower', 'blog']

