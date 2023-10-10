import pytest

from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from tests import conftest


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestCT03:
    def test_ct03_adicionar_produtos_carrinho(self):
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

