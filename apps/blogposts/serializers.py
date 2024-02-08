from django.contrib.auth import get_user_model
from rest_framework import serializers

from blogposts.models import Post, Blog

User = get_user_model()


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id', 'user']


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'creation_date',
            'blog'
        ]

