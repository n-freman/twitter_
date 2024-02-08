from django.contrib.auth import get_user_model
from rest_framework import viewsets

from blogposts.serializers import BlogSerializer, PostSerializer
from blogposts.models import Blog, Post


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows viewing blog objects.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows crud operations with posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

