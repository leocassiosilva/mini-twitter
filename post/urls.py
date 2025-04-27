from django.urls import include, path
from post.viewsets.post_viewset import PostViewSet
from rest_framework import routers

post_router = routers.DefaultRouter()
post_router.register(r'post', PostViewSet, basename='post')




urlpatterns = [
    path("", include(post_router.urls)),
]