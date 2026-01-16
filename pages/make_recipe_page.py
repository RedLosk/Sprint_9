import allure
from helpers import Helpers
from locators.make_recipe_page_locators import RecipePageLocators
from pages.base_page import BasePage


class MakeRecipePage(BasePage):

    @allure.step("Создать рецепт")
    def fill_recipe_form(self, recipe_data):
        self.check_element_visible(RecipePageLocators.RECIPE_NAME_INPUT)
        self.fill_element_with_value(RecipePageLocators.RECIPE_NAME_INPUT, recipe_data['title'])
        for mealtime_tag in ("Завтрак", "Обед", "Ужин"):
            if mealtime_tag in recipe_data['tags']:
                tag_locator = self.get_locator_with_value(RecipePageLocators.TAG_CHECKBOX, mealtime_tag)
                tag_element = self.check_element_visible(tag_locator)
                tag_element.click()
        for ingredient_item in recipe_data['ingredients']:
            self.fill_element_with_value(RecipePageLocators.INGREDIENT_INPUT, ingredient_item[0])
            ingredient_option_locator = self.get_locator_with_value(
                RecipePageLocators.INGREDIENT_SUGGESTION_ITEM,
                ingredient_item[0],
            )
            try:
                ingredient_option = self.check_element_visible(ingredient_option_locator, timeout=2)
                ingredient_option.click()
            except AssertionError:
                pass
            self.fill_element_with_value(RecipePageLocators.INGREDIENT_QUANTITY_INPUT, ingredient_item[1])
            self.click_element(RecipePageLocators.ADD_INGREDIENT_BUTTON)
        self.fill_element_with_value(RecipePageLocators.RECIPE_COOKING_TIME_INPUT, recipe_data['cook_time'])
        self.fill_element_with_value(RecipePageLocators.RECIPE_DESCRIPTION_INPUT, recipe_data['description'])
        photo_file_path = f"{Helpers.get_root_dir()}/assets/{recipe_data['image']}"
        self.fill_element_with_value(RecipePageLocators.FILE_INPUT, photo_file_path, False)
        self.click_element(RecipePageLocators.CREATE_RECIPE_BUTTON)
