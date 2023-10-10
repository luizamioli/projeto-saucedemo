import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from tests import conftest


@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_ct01_login_valido(self):

        login_page = LoginPage()
        home_page = HomePage()

        login_page.fazer_login("standard_user", "secret_sauce")

        home_page.verificar_login_sucesso()

