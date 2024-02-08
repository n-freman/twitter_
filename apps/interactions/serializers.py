from rest_framework import serializers

from interactions.models import PostRead, Follow


class PostReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostRead
        fields = ['id', 'post', 'user']


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = ['id', 'user', 'blog']

