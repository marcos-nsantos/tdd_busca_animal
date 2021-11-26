from django.test import TestCase, RequestFactory
from django.db.models import QuerySet


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_index_retorna_caracteristicas_do_animal(self):
        """Teste que verifica se o index retorna as caracteristicas do animal pesquisado"""
        response = self.client.get('/', {'caracteristicas': 'resultado'})
        self.assertIs(type(response.context['caracteristicas']), QuerySet)
