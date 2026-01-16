import allure
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


class TestRegisterPage:

    @allure.title("Проверка создания аккаунта")
    def test_user_can_create_new_account(self, driver):
        login_page, register_page = LoginPage(driver), RegisterPage(driver)
        login_page.open()
        login_page.navigate_to_signup_page()
        register_page.perform_signup()
        assert "/signin" in login_page.get_current_url()
        assert "Войти на сайт" == login_page.retrieve_page_heading()
