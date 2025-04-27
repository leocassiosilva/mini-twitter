from django.contrib import admin

from ..models import Relacionamento


@admin.register(Relacionamento)
class RelacionamentoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'seguidor',
        'seguindo',
        'data_criacao',
        'data_atualizacao', 

    ]

    autocomplete_fields = [
        'seguidor',
        'seguindo',
    ]

    readonly_fields = [
        'data_criacao',
        'data_atualizacao',
    ]

    fieldsets = (
        (None, {
            'fields': (
                'seguidor',
                'seguindo',
            )
        }),
        ('Informações de criação', {
            'fields': (
                'data_criacao',
            )
        }),
        ('Informações de atualização', {
            'fields': (
                'data_atualizacao',
            )
        }),
    )