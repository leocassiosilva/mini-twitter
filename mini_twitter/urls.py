from django.contrib import admin
from django.urls import path, include   
from rest_framework import permissions

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, serializers, viewsets

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Documentação Api Desafio Mini Twiter",
    #   terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email=""),
      license=openapi.License(name="Desafio Mini Twiter"),
   ),
   public=True,
    permission_classes=(permissions.AllowAny,),

   )

router = routers.DefaultRouter()


# router.register(r'user', ExperienciaViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("", include("core.urls")),
    path("", include("post.urls")),

]
