from django.db import models
from django.contrib.auth.models import User


class Relacionamento(models.Model):
    
    seguidor = models.ForeignKey(
        User, 
        related_name='seguindo', 
        on_delete=models.CASCADE
    )

    seguindo = models.ForeignKey(
        User, 
        related_name='seguindo_por', 
        on_delete=models.CASCADE
    )

    data_criacao = models.DateTimeField(
        verbose_name='Data de criação',
        auto_now_add=True
    )

    data_atualizacao = models.DateTimeField(
        verbose_name='Data de atualização',
        auto_now=True
    )

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return f"{self.seguidor.username} segue {self.seguindo.username}"

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'core'
        verbose_name = 'Relacionamento'
        verbose_name_plural = 'Relacionamentos'
        unique_together = ('seguidor', 'seguindo')  


