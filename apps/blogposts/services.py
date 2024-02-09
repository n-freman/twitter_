from blogposts.models import Post
from django.db.models import Subquery
from interactions.models import Follow


class PostsFeedService:
    
    @staticmethod
    def get_posts_feed_for_user(user_id):
        user_follows = Follow.objects.filter(
            follower__id=user_id
        ).values('id')
        return Post.objects.filter(
            blog__follows__in=Subquery(user_follows)
        ).order_by('-creation_date')

