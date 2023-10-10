import time

import pytest

from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from tests import conftest


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.realizar_compra
class TestCT04:
    def test_ct04_realizar_compra(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        produto_1 = "Sauce Labs Backpack"
        produto_2 = "Sauce Labs Bike Light"
        login_page.fazer_login("standard_user", "secret_sauce")
        home_page.adicionar_ao_carrinho_labs_backpack(produto_1)

        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carinho_labs_backpack(produto_1)

        carrinho_page.clicar_contiuar_comprando()
        home_page.adicionar_ao_carrinho_labs_bike(produto_2)
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carinho_labs_bike(produto_2)
        carrinho_page.verificar_produto_carinho_labs_backpack(produto_1)
        time.sleep(2)
        carrinho_page.clicar_botao_checkout()
        carrinho_page.inserir_informaçoes_checkout("Luiza", "Mioli", "90050340")
        carrinho_page.verificar_pagina_checkout()
        carrinho_page.clilca_botao_finish()
        carrinho_page.verificar_pagina_sucesso_compra()
