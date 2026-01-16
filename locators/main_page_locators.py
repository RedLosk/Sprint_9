from selenium.webdriver.common.by import By
from locators.common_locators import CommonLocators


class MainPageLocators(CommonLocators):

    LOGOUT_MENU_ITEM = (By.XPATH, "//*[contains(@class, 'styles_menuLink') and text()='Выход']")
    NEW_RECIPE_LINK = (By.XPATH, "//*[contains(@class, 'style_link') and text()='Создать рецепт']")
    DISH_CARD_CONTAINER = (By.XPATH, "//*[contains(@class, 'style_container')]/*[contains(@class, 'styles_single-card')]")
    DISH_NAME_TEXT = (By.XPATH, "//*[contains(@class, 'styles_single-card__title')]")
