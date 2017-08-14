import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        # Satisfeita, ela volta a dormir.
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """
        Edith ouviu sobre um novo App online para listas de tarefas muito
        legal! Ela vai dar uma olhada na homepage
        """
        self.browser.get('http://localhost:8000')

        # Ela notou que o título e o cabeçalho da página diz Listas de Tarefas
        self.assertIn('Listas de Tarefas', self.browser.title)
        self.fail('Finish the test!')

        # Ela é imediatamente convidada a colocar uma tarefa na lista

        # Ela digita "Comprar coxinhas" em uma caixa de texto (Edith é uma
        # PyLady)

        # Quando ela tecla Enter, a página atualiza, e agora a página lista
        # "1: Comprar coxinha" como um item em uma lista de tarefas

        # Ainda tem uma caixa de texto convidando-a a adicionar um outro item.
        # Ela digita "Comer as coxinhas" (Edith é muito metódica)

        # A página atualiza novamente, e agora mostra ambos os itens na lista
        # dela

        # Edith se pergunta se o site lembrará da sua lista. Então ela vê que o
        # site gerou uma URL única para ela - Tem um texto explicativo para
        # esse efeito.

        # Ela visita a URL - Sua lista de tarefas ainda está lá.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
