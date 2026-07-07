import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from urls import Urls


class LoginPage(BasePage):
    @allure.step("Открыть страницу логина")
    def open_login_page(self):
        self.open_url(Urls.LOGIN_PAGE)

    @allure.step("Авторизоваться")
    def login(self, email, password):
        self.set_text_to_element(LoginPageLocators.EMAIL_INPUT, email)
        self.set_text_to_element(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)