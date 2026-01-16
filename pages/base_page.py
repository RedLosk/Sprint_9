import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    @staticmethod
    def get_locator_with_value(locator_template, value):
        locator = (locator_template[0], locator_template[1].format(value))
        return locator

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Получить адрес текущей страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Проверить невидимость элемента с заданным локатором")
    def check_element_invisible(self, locator, timeout=-1):
        try:
            if timeout < 0:
                timeout = self.driver.timeout
            return WebDriverWait(self.driver, timeout).until(
                ec.invisibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Не найден невидимый элемент с заданным локатором")

    @allure.step("Проверить видимость элемента с заданным локатором")
    def check_element_visible(self, locator, timeout=-1):
        try:
            if timeout < 0:
                timeout = self.driver.timeout
            return WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Не найден видимый элемент с заданным локатором")

    @allure.step("Проверить наличие элемента с заданным локатором")
    def check_element_present(self, locator, timeout=-1):
        try:
            if timeout < 0:
                timeout = self.driver.timeout
            return WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Не найден элемент с заданным локатором")

    @allure.step("Проверить кликабельность элемента с заданным локатором")
    def check_element_clickable(self, locator):
        try:
            return WebDriverWait(self.driver, self.driver.timeout).until(
                ec.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError("Не найден кликабельный элемент с заданным локатором")

    @allure.step("Получить текст элемента с заданным локатором")
    def get_element_text(self, locator):
        element = self.check_element_visible(locator)
        text = element.text
        with allure.step(f"Получен текст: \'{text}\'"):
            return text

    @allure.step("Кликнуть по элементу с заданным локатором")
    def click_element(self, locator):
        element = self.check_element_clickable(locator)
        element.click()
        return element

    @allure.step("Заполнить заданным значением элемент с заданным локатором")
    def fill_element_with_value(self, locator, value, visible=True):
        if visible:
            element = self.check_element_visible(locator)
        else:
            element = self.check_element_present(locator)
        element.send_keys(value)
