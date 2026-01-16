import allure
from helpers import Helpers
from locators.register_page_locators import RegisterPageLocators
from pages.base_page import BasePage


class RegisterPage(BasePage):

    @allure.step("Открыть страницу регистрации")
    def open(self):
        self.driver.get(f"{self.driver.base_url}/signup")
        self.check_element_visible(RegisterPageLocators.SIGNUP_PAGE_HEADING)

    @allure.step("Перейти на страницу авторизации")
    def navigate_to_signin_page(self):
        self.click_element(RegisterPageLocators.NAVIGATION_SIGNIN_LINK)
        self.check_element_invisible(RegisterPageLocators.SIGNUP_PAGE_HEADING)

    @allure.step("Создать аккаунт")
    def perform_signup(self, user=None):
        user_data = Helpers.generate_random_user() if user is None else dict(user)
        self.check_element_visible(RegisterPageLocators.SIGNUP_PAGE_HEADING)
        self.fill_element_with_value(RegisterPageLocators.FIRSTNAME_FIELD, user_data['first_name'])
        self.fill_element_with_value(RegisterPageLocators.LASTNAME_FIELD, user_data['last_name'])
        self.fill_element_with_value(RegisterPageLocators.USERNAME_FIELD, user_data['username'])
        self.fill_element_with_value(RegisterPageLocators.EMAIL_FIELD, user_data['email'])
        self.fill_element_with_value(RegisterPageLocators.PASSWORD_FIELD, user_data['password'])
        self.click_element(RegisterPageLocators.SUBMIT_SIGNUP_BUTTON)
        self.check_element_invisible(RegisterPageLocators.SIGNUP_PAGE_HEADING)
        return user_data
