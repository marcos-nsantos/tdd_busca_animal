import os

from django.test import LiveServerTestCase
from selenium import webdriver


class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Edge(executable_path=f'{os.getcwd()}/msedgedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_buscando_um_novo_animal(self):
        """Teste se um usuário encontra um animal pesquisando"""

        # Vini, deseja encontrar um novo animal,
        # para adotar.

        # Ele encontra o Busca Animal e decide usar o site,
        home_page = self.browser.get(self.live_server_url + '/')

        # porque ele vê no menu do site escrito Busca Animal.
        brand_element = self.browser.find_element_by_css_selector('.navbar')
        self.assertEqual('Busca Animal', brand_element.text)

        # Ele vê um campo para pesquisar animais pelo nome.
        buscar_animal_input = self.browser.find_element_by_css_selector('input#buscar_animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: Leão, Uso')

        # Ele pesquisa por Leão e clica no botão pesquisar.
        buscar_animal_input.send_keys('Leão')
        self.browser.find_element_by_css_selector('form button').click()

        # O site exibe 4 caracteristicas do animal pesquisado.
        caracticas = self.browser.find_elements_by_css_selector('.result-description')
        self.assertGreater(len(caracticas), 3)

        # Ele desiste de adotar um leão.
