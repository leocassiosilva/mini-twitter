from django.contrib import admin

from ..models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'titulo',
        'conteudo',
        'imagem',
        'data_criacao', 
        'data_atualizacao',
    ]

    search_fields = [
        'id',
        'titulo',
        'conteudo',
    ]

    list_filter = [
        'usuario_criacao',
    ]

    readonly_fields = [
        'data_criacao',
        'data_atualizacao',
        'usuario_criacao',
        'usuario_atualizacao',
    ]

    filter_horizontal = [
        'curtidas',
    ]

    fieldsets = (
        (None, {
            'fields': (
                'titulo',
                'conteudo',
                'imagem',
            )
        }),
        ('Informações de criação', {
            'fields': (
                'data_criacao',
                'usuario_criacao',
            )
        }),
        ('Informações de atualização', {
            'fields': (
                'data_atualizacao',
                'usuario_atualizacao',
            )
        }),
    )