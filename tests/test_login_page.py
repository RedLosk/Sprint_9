import allure
from data import Data
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.register_page import RegisterPage


class TestLoginPage:

    @allure.title("Проверка авторизации")
    def test_user_can_signin_successfully(self, driver):
        login_page, main_page, register_page = LoginPage(driver), MainPage(driver), RegisterPage(driver)
        register_page.open()
        register_page.navigate_to_signin_page()
        login_page.perform_signin(Data.USER)
        assert "/recipes" in main_page.get_current_url()
        assert main_page.retrieve_logout_button().is_displayed()
