from selenium.webdriver.common.by import By
from locators.common_locators import CommonLocators


class LoginPageLocators(CommonLocators):

    SIGNIN_PAGE_HEADING = (By.XPATH, "//*[contains(@class, 'styles_title') and text()='Войти на сайт']")
    SUBMIT_SIGNIN_BUTTON = (By.XPATH, "//*[contains(@class, 'style_button') and text()='Войти']")
