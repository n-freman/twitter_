"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from blogposts.urls import router as blogposts_router
from blogposts.views import PostFeedView
from django.contrib import admin
from django.urls import include, path
from interactions.urls import router as interactions_router
from rest_framework.routers import DefaultRouter
from users.urls import router as users_router

router = DefaultRouter()

router.registry.extend(interactions_router.registry)
router.registry.extend(users_router.registry)
router.registry.extend(blogposts_router.registry)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    path('api/posts-feed/<int:user_id>/', PostFeedView.as_view())
]

