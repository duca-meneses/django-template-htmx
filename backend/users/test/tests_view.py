# No seu arquivo de testes (por exemplo, test_views.py)
from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.urls import reverse

from users.views import profile_view


class ProfileViewTestCase(TestCase):
    def setUp(self):
        # Crie um usuário de teste
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )

        # Crie uma instância de perfil associada ao usuário
        self.user.profile.bio = 'Este é o meu perfil de teste.'
        self.user.profile.save()

        # Crie uma fábrica de solicitações
        self.factory = RequestFactory()

    def test_profile_view_authenticated_user(self):
        # Crie uma solicitação GET para a página de perfil
        request = self.factory.get(reverse('profile'))
        request.user = self.user

        # Chame a função de visualização
        response = profile_view(request)

        # Verifique se a resposta tem o status HTTP 200 (OK)
        assert response.status_code == HTTPStatus.OK

        # Verifique se o conteúdo da página contém a bio do perfil
        self.assertInHTML(request.user.username, str(response.content))

    def test_profile_view_unauthenticated_user(self):
        # Crie uma solicitação GET para a página de perfil sem usuário autenticado
        request = self.factory.get(reverse('profile'))

        # Chame a função de visualização
        response = profile_view(request)

        # Verifique se a resposta tem o status HTTP 302
        # (redirect para a página de login)
        assert response.status_code == HTTPStatus.FOUND
        assert response.url == reverse('account_login')
