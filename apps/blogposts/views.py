from blogposts.models import Blog, Post
from blogposts.serializers import BlogSerializer, PostSerializer
from blogposts.services import PostsFeedService
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.settings import api_settings


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


class PostFeedViewSet(
    viewsets.GenericViewSet
):
    serializer_class = PostSerializer
    service = PostsFeedService

    def retrieve(self, request, pk, *args, **kwargs):
        print(f'PK: {pk}')
        queryset = self.service.get_posts_feed_for_user(pk)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PostFeedView(APIView):
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    serializer_class = PostSerializer
    service = PostsFeedService

    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
         """
         Return a single page of results, or `None` if pagination is disabled.
         """
         if self.paginator is None:
             return None
         return self.paginator.paginate_queryset(
            queryset,
            self.request,
            view=self
        )

    def get_paginated_response(self, data):
         """
         Return a paginated style `Response` object for the given output data.
         """
         assert self.paginator is not None
         return self.paginator.get_paginated_response(data) 

    def get(self, request, user_id):
        queryset = self.service.get_posts_feed_for_user(user_id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

