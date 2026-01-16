import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Получить элемент кнопки 'Выход'")
    def retrieve_logout_button(self):
        return self.check_element_visible(MainPageLocators.LOGOUT_MENU_ITEM)

    @allure.step("Перейти на страницу создания рецепта")
    def navigate_to_new_recipe_page(self):
        self.click_element(MainPageLocators.NEW_RECIPE_LINK)

    @allure.step("Получить элемент карточки рецепта")
    def retrieve_dish_card(self):
        return self.check_element_visible(MainPageLocators.DISH_CARD_CONTAINER)

    @allure.step("Получить название рецепта")
    def retrieve_dish_name(self):
        return self.get_element_text(MainPageLocators.DISH_NAME_TEXT)
