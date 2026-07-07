import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.orders_page import OrdersPage


@allure.feature("Лента заказов")
class TestOrdersPage:

    @allure.title("После создания заказа счётчик Выполнено за всё время увеличивается")
    def test_total_orders_counter_increases_after_create_order(self, driver, user):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        orders_page = OrdersPage(driver)

        orders_page.open_orders_page()
        counter_before = orders_page.get_total_orders_counter()

        login_page.open_login_page()
        login_page.login(user["email"], user["password"])
        main_page.add_first_ingredient_to_order()
        main_page.create_order()
        main_page.get_order_number()
        main_page.close_order_modal()

        orders_page.open_orders_page()
        orders_page.refresh_orders_page()
        orders_page.wait_for_total_orders_counter_changed(counter_before)
        counter_after = orders_page.get_total_orders_counter()

        assert counter_after > counter_before

    @allure.title("После создания заказа счётчик Выполнено за сегодня увеличивается")
    def test_today_orders_counter_increases_after_create_order(self, driver, user):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        orders_page = OrdersPage(driver)

        orders_page.open_orders_page()
        counter_before = orders_page.get_today_orders_counter()

        login_page.open_login_page()
        login_page.login(user["email"], user["password"])
        main_page.add_first_ingredient_to_order()
        main_page.create_order()
        main_page.get_order_number()
        main_page.close_order_modal()

        orders_page.open_orders_page()
        orders_page.refresh_orders_page()
        orders_page.wait_for_today_orders_counter_changed(counter_before)
        counter_after = orders_page.get_today_orders_counter()

        assert counter_after > counter_before

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_created_order_number_appears_in_work_section(self, driver, user):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        orders_page = OrdersPage(driver)

        login_page.open_login_page()
        login_page.login(user["email"], user["password"])
        main_page.add_first_ingredient_to_order()
        main_page.create_order()
        order_number = main_page.get_order_number()
        main_page.close_order_modal()
        orders_page.open_orders_page()

        assert orders_page.is_order_number_in_work(order_number)