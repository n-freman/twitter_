from blogposts.views import BlogViewSet, PostViewSet
from rest_framework.routers import DefaultRouter

router  = DefaultRouter()

router.register(r'blogs', BlogViewSet)
router.register(r'posts', PostViewSet)

