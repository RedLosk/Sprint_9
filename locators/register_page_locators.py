from selenium.webdriver.common.by import By
from locators.common_locators import CommonLocators


class RegisterPageLocators(CommonLocators):

    SIGNUP_PAGE_HEADING = (By.XPATH, "//*[contains(@class, 'styles_title') and text()='Регистрация']")
    FIRSTNAME_FIELD = (By.XPATH, "//*[contains(@class, 'styles_inputField') and @name='first_name']")
    LASTNAME_FIELD = (By.XPATH, "//*[contains(@class, 'styles_inputField') and @name='last_name']")
    USERNAME_FIELD = (By.XPATH, "//*[contains(@class, 'styles_inputField') and @name='username']")
    SUBMIT_SIGNUP_BUTTON = (By.XPATH, "//*[contains(@class, 'style_button') and text()='Создать аккаунт']")
