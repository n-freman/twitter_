from interactions.views import FollowViewSet, PostReadViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(f'follows', FollowViewSet)
router.register(f'post-read', PostReadViewSet)

