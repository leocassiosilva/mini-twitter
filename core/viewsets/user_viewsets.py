from core.serializers.user_serializers import UserSerializer
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'username',
        'email',
        'first_name',
        'last_name'
    ]

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]