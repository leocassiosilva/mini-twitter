from rest_framework import serializers

from ..models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [  
            'id',
            'titulo',
            'conteudo',
            'data_criacao',
            'data_atualizacao',
            'nome_usuario_criacao',
            'nome_usuario_atualizacao',
            'curtidas',
            'curtidas_count',
        ]
        read_only_fields = [
            'data_criacao',
            'data_atualizacao',
            'usuario_criacao',
            'usuario_atualizacao',
        ]