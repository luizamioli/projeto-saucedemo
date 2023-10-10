import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from tests import conftest


@pytest.mark.usefixtures("setup_teardown")
class TestCT02:
    def test_ct02_login_valido(self):
        mensagem_errro_esperada = "Epic sadface: Username and password do not match any user in this service"

        login_page = LoginPage()
        home_page = HomePage()

        login_page.fazer_login("standard_user", "senhaerrada")

        login_page.verificar_mensagem_error_login_existe()
        login_page.verificar_texto_mensagem_erro_login(mensagem_errro_esperada)