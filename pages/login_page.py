import allure
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Открыть страницу авторизации")
    def open(self):
        self.driver.get(f"{self.driver.base_url}/signin")
        self.check_element_visible(LoginPageLocators.SIGNIN_PAGE_HEADING)

    @allure.step("Перейти на страницу регистрации")
    def navigate_to_signup_page(self):
        self.click_element(LoginPageLocators.NAVIGATION_SIGNUP_LINK)
        self.check_element_invisible(LoginPageLocators.SIGNIN_PAGE_HEADING)

    @allure.step("Войти в аккаунт")
    def perform_signin(self, user):
        self.fill_element_with_value(LoginPageLocators.EMAIL_FIELD, user['email'])
        self.fill_element_with_value(LoginPageLocators.PASSWORD_FIELD, user['password'])
        self.click_element(LoginPageLocators.SUBMIT_SIGNIN_BUTTON)
        self.check_element_invisible(LoginPageLocators.SIGNIN_PAGE_HEADING)

    @allure.step("Получить текст заголовка")
    def retrieve_page_heading(self):
        return self.get_element_text(LoginPageLocators.PAGE_HEADING)
