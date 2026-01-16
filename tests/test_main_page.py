import allure
from data import Data
from pages.make_recipe_page import MakeRecipePage
from pages.main_page import MainPage


class TestMainPage:

    @allure.title("Проверка создания рецепта")
    def test_user_can_add_new_dessert_recipe(self, authenticated_session):
        main_page, make_recipe_page = MainPage(authenticated_session), MakeRecipePage(authenticated_session)
        main_page.navigate_to_new_recipe_page()
        make_recipe_page.fill_recipe_form(Data.RECIPE)
        assert main_page.retrieve_dish_card().is_displayed()
        assert main_page.retrieve_dish_name() == Data.RECIPE['title']
