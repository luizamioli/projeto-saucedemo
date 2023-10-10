from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests import conftest


class CarrinhoPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.item_inventario_labs_backpack = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.item_inventario_labs_bike = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.botao_continuar_comprando = (By.ID, "continue-shopping")
        self.botao_checkout = (By.ID, "checkout")
        self.botao_continue = (By.ID, "continue")
        self.campo_nome_checkout = (By.ID, "first-name")
        self.campo_sobrenome_checkout = (By.ID, "last-name")
        self.campo_cep = (By.ID, "postal-code")
        self.titulo_pagina_checkout = (By.XPATH,  "//span[@class='title']")
        self.botao_finish = (By.ID, "finish")
        self.titulo_pagina_sucesso = (By.XPATH, "//h2[@class='complete-header']")

    def verificar_produto_carinho_labs_backpack(self, nome_item):
        """
        Verifica se o produto Sauce Labs Backpack existe
        """
        item = (self.item_inventario_labs_backpack[0], self.item_inventario_labs_backpack[1].format(nome_item))
        self.verificar_elemento_existe(item)

    def verificar_produto_carinho_labs_bike(self, nome_item):
        """
        Verifica se o produto Labs Bike existe
        """
        item = (self.item_inventario_labs_bike[0], self.item_inventario_labs_bike[1].format(nome_item))
        self.verificar_elemento_existe(item)

    def verificar_pagina_checkout(self):
        """
        Verifica se o login foi realizado com sucesso
        """
        self.verificar_elemento_existe(self.titulo_pagina_checkout)

    def verificar_pagina_sucesso_compra(self):
        """
        Verifica se a compra foi realizada com sucessos
        """
        self.verificar_elemento_existe(self.titulo_pagina_sucesso)

    def clicar_contiue_checkout(self):
        """
        Clilca no botão 'Continue' na página de checkout
        """
        self.clilcar(self.botao_continue)

    def clilca_botao_finish(self):
        """
        Clilca no botão 'Finish'
        """

        self.clilcar(self.botao_finish)

    def clicar_contiuar_comprando(self):
        """
        Clilca no botão 'Continue Shopping'
        """
        self.clilcar(self.botao_continuar_comprando)

    def clicar_botao_checkout(self):
        """
        Clilca no botão 'Continue Shopping'
        """
        self.clilcar(self.botao_checkout)

    def inserir_informaçoes_checkout(self, nome: str, sobrenome: str, cep: str):
        """
        Digita nome, sobrenome e CEP
        """
        self.escrever(self.campo_nome_checkout, nome)
        self.escrever(self.campo_sobrenome_checkout, sobrenome)
        self.escrever(self.campo_cep, cep)
        self.clilcar(self.botao_continue)





