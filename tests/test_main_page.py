import allure

from pages.main_page import MainPage
from pages.orders_page import OrdersPage
from urls import Urls


@allure.feature("Основная функциональность")
class TestMainPage:

    @allure.title("Переход по клику на Конструктор")
    def test_click_constructor_button_open_constructor(self, driver):
        main_page = MainPage(driver)
        orders_page = OrdersPage(driver)

        orders_page.open_orders_page()
        main_page.click_constructor_button()

        assert Urls.BASE_URL in main_page.get_current_url()

    @allure.title("Переход по клику на Лента заказов")
    def test_click_orders_button_open_orders_page(self, driver):
        main_page = MainPage(driver)
        orders_page = OrdersPage(driver)

        main_page.open_main_page()
        main_page.click_orders_button()

        assert orders_page.is_orders_page_opened()

    @allure.title("При клике на ингредиент открывается модальное окно")
    def test_click_ingredient_open_modal(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_first_ingredient()

        assert main_page.is_ingredient_modal_visible()

    @allure.title("Модальное окно ингредиента закрывается по клику на крестик")
    def test_close_ingredient_modal_by_cross(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_first_ingredient()
        main_page.close_ingredient_modal()

        assert main_page.wait_for_ingredient_modal_closed()

    @allure.title("При добавлении ингредиента в заказ счётчик увеличивается")
    def test_add_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        counter_before = main_page.get_first_ingredient_counter()
        main_page.add_first_ingredient_to_order()
        counter_after = main_page.get_first_ingredient_counter()

        assert counter_after > counter_before