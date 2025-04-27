from rest_framework import serializers

from ..models import Relacionamento


class RelacionamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relacionamento
        fields = '__all__'
        read_only_fields = [
            'id', 
            'data_criacao', 
            'data_atualizacao'
        ]