from selenium.webdriver.common.by import By


class CommonLocators:

    NAVIGATION_SIGNIN_LINK = (By.XPATH, "//*[contains(@class, 'style_link') and text()='Войти']")
    NAVIGATION_SIGNUP_LINK = (By.XPATH, "//*[contains(@class, 'style_link') and text()='Создать аккаунт']")
    PAGE_HEADING = (By.XPATH, "//*[contains(@class, 'styles_title') and text()]")
    EMAIL_FIELD = (By.XPATH, "//*[contains(@class, 'styles_inputField') and @name='email']")
    PASSWORD_FIELD = (By.XPATH, "//*[contains(@class, 'styles_inputField') and @name='password']")
