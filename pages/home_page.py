from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests import conftest


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "//span[@class='title']")
        self.icone_carrinho = (By.ID, "shopping_cart_container")
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.btn_adicionar_carrinho_labs_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.btn_adicionar_carrinho_labs_bike = (By.ID, "add-to-cart-sauce-labs-bike-light")

    def verificar_login_sucesso(self):
        """
        Verifica se o login foi realizado com sucesso
        """
        self.verificar_elemento_existe(self.titulo_pagina)

    def acessar_carrinho(self):
        """
        Acessa o carrinho pelo ícone
        """
        self.clilcar(self.icone_carrinho)

    def adicionar_ao_carrinho_labs_backpack(self, nome_item):
        """
        Adiciona o produto 'Sauce Labs Backpack' ao carrinho
        """
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.clilcar(item)
        self.clilcar(self.btn_adicionar_carrinho_labs_backpack)

    def adicionar_ao_carrinho_labs_bike(self, nome_item):
        """
        Adiciona o produto 'Sauce Labs Bike Light' ao carrinho
        """
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.clilcar(item)
        self.clilcar(self.btn_adicionar_carrinho_labs_bike)
