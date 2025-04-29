from django.test import TestCase
from django.contrib.auth.models import User



class TestUserModel(TestCase):
    
    # Teste para criar um usuario
    def teste_create_user(self):
        """
        Teste para criar um usuario
        """
        # Criando um usuario de teste
        user  = User.objects.create(
            username='testuser',
            email='teste@gmail.com',
            password='testpassword',
            first_name='Test',
            last_name='User'
        )
    
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'teste@gmail.com')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')
        
    
    