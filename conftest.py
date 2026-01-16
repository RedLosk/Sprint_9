import os
import pytest
from data import Data
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture(params=["remote"])
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--window-size=1920,1080")
    if request.param == "local":
        driver = webdriver.Chrome(options=options)
    else:
        selenoid_url = os.getenv("SELENOID_URL", "http://localhost:4444/wd/hub")
        driver = webdriver.Remote(command_executor=selenoid_url, options=options)
    driver.set_window_size(1920, 1080)
    driver.base_url = Data.BASE_URL
    driver.timeout = 5
    yield driver
    driver.quit()

@pytest.fixture
def authenticated_session(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.perform_signin(Data.USER)
    return driver

