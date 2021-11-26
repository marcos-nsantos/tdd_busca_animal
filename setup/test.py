import os

from django.test import LiveServerTestCase
from selenium import webdriver


class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Edge(executable_path=f'{os.getcwd()}/msedgedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_deu_ruim(self):
        """teste de exemplo de erro"""
        self.fail('Teste falhou - deu ruim mesmo')
