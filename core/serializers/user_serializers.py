from core.models.relacionamento_models import Relacionamento
from rest_framework import serializers

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    seguidores = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'seguidores',  
        ]
        read_only_fields = ['id']
    
        def get_seguidores(self, obj):
            """Método para obter o número de seguidores de um usuário"""
            quantidade_seguidores = Relacionamento.objects.filter(seguindo=obj).count()
            return quantidade_seguidores