from django.test import TestCase

from post.models.post_models import Post



class PostModelTestCase(TestCase):
    
    def teste_create_post(self):
        # 
        post = Post.objects.create(
            titulo="Test Post", 
            conteudo="Um Post para realizar um teste.", 
        )
        
        self.assertIsInstance(post, Post)
        self.assertEqual(post.titulo, "Test Post")
        self.assertEqual(post.conteudo, "Um Post para realizar um teste.")
        
        
