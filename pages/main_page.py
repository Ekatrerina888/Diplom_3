import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from urls import Urls


class MainPage(BasePage):
    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open_url(Urls.MAIN_PAGE)


    @allure.step("Кликнуть на кнопку Конструктор")
    def click_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)


    @allure.step("Кликнуть на кнопку Лента заказов")
    def click_orders_button(self):
        self.click_on_element(MainPageLocators.ORDERS_BUTTON)


    @allure.step("Кликнуть на первый ингредиент")
    def click_first_ingredient(self):
        self.click_on_element(MainPageLocators.FIRST_INGREDIENT)


    @allure.step("Проверить, что модальное окно ингредиента отображается")
    def is_ingredient_modal_visible(self):
        return self.find_visible_element(MainPageLocators.INGREDIENT_MODAL).is_displayed()
    

    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        self.click_on_element(MainPageLocators.INGREDIENT_MODAL_CLOSE_BUTTON)


    @allure.step("Дождаться закрытия модального окна ингредиента и исчезновения затемнения")
    def wait_for_ingredient_modal_closed(self):
        return (
            self.wait_for_invisibility_of_element(MainPageLocators.INGREDIENT_MODAL)
            and self.wait_for_overlay_disappear(MainPageLocators.MODAL_OVERLAY)
        )


    @allure.step("Получить значение счётчика первого ингредиента")
    def get_first_ingredient_counter(self):
        counter_text = self.get_text_from_element(MainPageLocators.FIRST_INGREDIENT_COUNTER)
        return int(counter_text)
    

    @allure.step("Добавить первый ингредиент в заказ")
    def add_first_ingredient_to_order(self):
        self.drag_and_drop_with_js(
            MainPageLocators.FIRST_INGREDIENT,
            MainPageLocators.BURGER_CONSTRUCTOR
        )


    @allure.step("Оформить заказ")
    def create_order(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON)
        self.find_visible_element(MainPageLocators.ORDER_MODAL)


    @allure.step("Получить номер созданного заказа")
    def get_order_number(self):
        self.wait_for_text_not_in_element(MainPageLocators.ORDER_NUMBER, "9999", timeout=20)
        order_number_text = self.get_text_from_element(MainPageLocators.ORDER_NUMBER)
        return order_number_text.lstrip("0")
    

    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        self.click_on_element(MainPageLocators.ORDER_MODAL_CLOSE_BUTTON)
        self.wait_for_overlay_disappear(MainPageLocators.MODAL_OVERLAY)