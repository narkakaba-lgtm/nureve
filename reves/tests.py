from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Reve

class NureveAppTests(TestCase):

    def setUp(self):
        """Configuração inicial executada antes de cada teste."""
        # Cria um utilizador de testes
        self.user = User.objects.create_user(
            username='jean_reve', 
            password='PasswordSecura123!'
        )
        
        # Cria um sonho de testes privado
        self.reve_prive = Reve.objects.create(
            auteur=self.user,
            titre='Rêve de vol',
            contenu='Je volais au-dessus des nuages.',
            est_public=False
        )

    def test_creation_reve(self):
        """Garante que o modelo de Sonho guarda os dados corretamente."""
        self.assertEqual(self.reve_prive.titre, 'Rêve de vol')
        self.assertEqual(self.reve_prive.auteur.username, 'jean_reve')
        self.assertFalse(self.reve_prive.est_public)

    def test_page_accueil_accessible(self):
        """Garante que a página inicial abre com sucesso (Código HTTP 200)."""
        response = self.client.get(reverse('accueil'))
        self.assertEqual(response.status_code, 200)

    def test_page_espace_public_accessible(self):
        """Garante que o Espaço Público abre mesmo sem login."""
        response = self.client.get(reverse('espace_public'))
        self.assertEqual(response.status_code, 200)

    def test_journal_protege(self):
        """Garante que utilizadores não autenticados são redirecionados ao tentar ver o diário."""
        response = self.client.get(reverse('mes_reves'))
        # Deve redirecionar (HTTP 302) para a página de login
        self.assertEqual(response.status_code, 302)

    def test_journal_accessible_apres_connexion(self):
        """Garante que o diário abre corretamente após o login do utilizador."""
        self.client.login(username='jean_reve', password='PasswordSecura123!')
        response = self.client.get(reverse('mes_reves'))
        self.assertEqual(response.status_code, 200)
