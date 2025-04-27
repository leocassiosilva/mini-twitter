from core.models.relacionamento_models import Relacionamento
from post.serializers.post_serializer import PostSerializer
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from ..models import Post

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-data_criacao')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]
    pagination_class = LargeResultsSetPagination

    search_fields = [
        'titulo',
        'conteudo',
    ]

    def get_queryset(self):
        """
        Override the get_queryset method to filter the queryset based on the user.
        """
        # Pegar os objetos 'seguindo' dos relacionamentos
        usuarios = Relacionamento.objects.filter(seguidor=self.request.user).select_related('seguindo')

        
        usuarios_seguidos = usuarios.values_list('seguindo', flat=True)
        usuarios_seguidos = list(usuarios_seguidos) + [self.request.user.id]

        return Post.objects.filter(usuario_criacao__in=usuarios_seguidos).order_by('-data_criacao')