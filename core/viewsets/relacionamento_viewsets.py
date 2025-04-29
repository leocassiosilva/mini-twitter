from core.serializers.relacionamento_serializers import RelacionamentoSerializer
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from ..models import Relacionamento
from django.contrib.auth.models import User


class RelacionamentoViewSet(viewsets.ModelViewSet):
    queryset = Relacionamento.objects.all()
    serializer_class = RelacionamentoSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        relacionamentos = Relacionamento.objects.filter(seguidor=self.request.user)

        return relacionamentos
    

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def seguir(self, request, *args, **kwargs):
        """
        Método para seguir um usuário.
        """
        
        usuario_seguido = get_object_or_404(User, id=kwargs['pk'])

        if usuario_seguido == request.user:
            return Response({"message": "Você não pode seguir a si mesmo."}, status=400)    
        
        relacionamento, created = Relacionamento.objects.get_or_create(
            seguidor=request.user,
            seguindo=usuario_seguido
        )

        if created:
            return Response({"message": "Você começou a seguir o usuário."})
        else:
            return Response({"message": "Você já segue este usuário."}, status=400)



    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def deixar_seguir(self, request, *args, **kwargs):
        """
        Método para deixar de seguir um usuário.
        """
        
        usuario_seguido = get_object_or_404(User, id=kwargs['pk'])

        if usuario_seguido == request.user:
            return Response({"message": "Você não pode deixar de seguir a si mesmo."}, status=400)    
        
        relacionamento = get_object_or_404(
            Relacionamento,
            seguidor=request.user,
            seguindo=usuario_seguido
        )
        
        relacionamento.delete()

        return Response({"message": "Você deixou de seguir o usuário."})
        

    