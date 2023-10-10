from tests import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def encontrar_elemento(self, locator):
        """
        Econtra mais de um elemento na página
        :return o locator em questão
         """
        return self.driver.find_element(*locator)

    def encontrar_elementos(self, locator):
        """
        Econtra mais de um elemento na página
        :return o locator em questão
        """
        return self.driver.find_elements(*locator)

    def escrever(self, locator, text):
        """
        Escreve no locator
        """
        self.encontrar_elemento(locator).send_keys(text)

    def clilcar(self, locator):
        """
        Clica no locator indicado
        """
        self.encontrar_elemento(locator).click()

    def verificar_elemento_existe(self, locator):
        """
        Verifica se o elemento existe
        """
        assert self.encontrar_elemento(locator).is_displayed(), f"O elemento '{locator}' não foi encontrado na tela."

    def pegar_texto_elemento(self, locator):
        """
        Verifica o texto do elemento
        :return: o texto do elemeto
        """
        self.esperar_carregar_elemento(locator)
        return self.encontrar_elemento(locator).text

    def esperar_carregar_elemento(self, locator, timeout=10):
        """
        Espera o elemento carregar
        """
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(*locator))

    def verificar_elemento_existe(self, locator):
        """
        Verifica se o elemento existe na página
        """
        assert self.encontrar_elemento(
            locator), f"O elemento '{locator}' não foi encontrado mas é esperado que ele exista"

    def verificar_elemento_nao_existe(self, locator):
        """
        Verifica se o elemento não eixste
        """
        assert len(self.encontrar_elementos(
            locator)) == 0, f"O elemento '{locator}' foi encontrado mas é esperado que ele não exista"

    def clique_duplo(self, locator):
        """
        Clilca duas vezes no elemento
        """
        element = self.esperar_carregar_elemento(locator)
        ActionChains(self.driver).double_click(element).perform()

    def clique_botao_direito(self, locator):
        """
        Clilca no botão direito do mouse
        """
        element = self.esperar_carregar_elemento(locator)
        ActionChains(self.driver).context_click(element).perform()

    def pressionar_tecla(self, locator, key):
        """
        Pressiona a tecla indicada
        """
        element = self.encontrar_elemento(locator)
        if key == "ENTER":
            element.send_keys(Keys.ENTER)
        elif key == "ESPAÇO":
            element.send_keys(Keys.SPACE)
