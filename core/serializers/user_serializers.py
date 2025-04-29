from core.models.relacionamento_models import Relacionamento
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    seguidores = serializers.SerializerMethodField()
    username = serializers.CharField(
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )

    password2 = serializers.CharField(
        write_only=True,
        required=True,
        label='Confirmação de Senha'
    )

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password2',
            'seguidores',  
        ]
        read_only_fields = ['id']
        
    def validate(self, attrs):
        """Método para validar os dados de entrada"""

        #Attrs é um dicionario com os dados de entrada
        #Verifica se as senhas são iguais
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {'password': 'As senhas não coincidem.'}
            )
        return attrs
    

    def create(self, validated_data):
        """Método para criar um novo usuário"""

        #Cria uma intancia do User com os dados validados
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        #Criptografa a senha e salva o usuário
        user.set_password(validated_data['password'])

        #salva o usuário no banco de dados
        user.save()

        #retorna o usuário criado
        return user
    
    def get_seguidores(self, obj):
        """Método para obter o número de seguidores de um usuário"""
        
        #Filtra os relacionamentos onde o usuário está sendo seguido
        quantidade_seguidores = Relacionamento.objects.filter(seguindo=obj).count()
        
        #Retorna a quantidade de seguidores
        return quantidade_seguidores