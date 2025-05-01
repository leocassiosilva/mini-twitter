from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    
    titulo = models.CharField(
        verbose_name='Título',
        max_length=250,
    )

    conteudo = models.TextField(
        verbose_name='Conteúdo',
    )

    imagem = models.ImageField(
        verbose_name='Imagem',
        upload_to='post/imagens/',
        blank=True,
        null=True,
    )
    
    data_criacao = models.DateTimeField(
        verbose_name='Data de criação',
        auto_now_add=True
    )
    
    data_atualizacao = models.DateTimeField(
        verbose_name='Data de atualização',
        auto_now=True
    )
    
    usuario_criacao = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name='Usuário de criação',
        blank=True,
        null=True,
    )
    
    usuario_atualizacao = models.ForeignKey(
        User,
        related_name='%(class)s_requests_modified',
        verbose_name='Usuário de atualização',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )


    curtidas = models.ManyToManyField(
        User, related_name='curtida_posts', 
        blank=True
    )

    @property
    def total_curtidas(self):
        '''Método que retorna o total de curtidas do post.'''
        return self.curtidas.count()
    

    @property
    def nome_usuario_criacao(self):
        '''Retorna o nome do usuário que criou o post.'''
        return self.usuario_criacao.username if self.usuario_criacao else None
    
    @property
    def nome_usuario_atualizacao(self):
        '''Retorna o nome do usuário que atualizou o post.'''
        return self.usuario_atualizacao.username if self.usuario_atualizacao else None

    @property
    def curtidas_count(self):
        '''Retorna a quantidade de curtidas do post.'''
        return self.curtidas.count()


    def save(self, *args, **kwargs):
        '''Sobrescrita do método save para realizarmos ações personalizadas.'''
        from crum import get_current_user
    
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
    
        super(Post, self).save(*args, **kwargs)
    


    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return self.titulo

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'post'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    