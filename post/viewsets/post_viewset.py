from post.serializers.post_serializer import PostSerializer
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]

    search_fields = [
        
    ]

    def get_queryset(self):
        """
        Override the get_queryset method to filter the queryset based on the user.
        """
        user = self.request.user
        return Post.objects.filter(usuario_criacao=user)