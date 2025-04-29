from django.urls import include, path
from core.viewsets.relacionamento_viewsets import RelacionamentoViewSet
from core.viewsets.user_viewsets import UserViewSet
from rest_framework import routers

core_router = routers.DefaultRouter()
core_router.register(r'user', UserViewSet)
core_router.register(r'relacionamento', RelacionamentoViewSet)




urlpatterns = [
    path("", include(core_router.urls)),
]