import allure
import pytest
from selenium import webdriver

from helpers import create_user, delete_user


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Choose browser: chrome or firefox"
    )


@pytest.fixture

def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture

def user():
    with allure.step("Создать пользователя через API"):
        user_data, access_token = create_user()

    yield user_data

    with allure.step("Удалить пользователя через API"):
        delete_user(access_token)