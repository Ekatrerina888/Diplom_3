import allure

from locators.orders_page_locators import OrdersPageLocators
from pages.base_page import BasePage
from urls import Urls



class OrdersPage(BasePage):
    @allure.step("Открыть страницу Лента заказов")
    def open_orders_page(self):
        self.open_url(Urls.ORDERS_PAGE)

    @allure.step("Проверить, что страница Лента заказов открыта")
    def is_orders_page_opened(self):
        return self.find_visible_element(OrdersPageLocators.ORDERS_HEADER).is_displayed()

    @allure.step("Получить значение счётчика Выполнено за всё время")
    def get_total_orders_counter(self):
        return int(self.get_text_from_element(OrdersPageLocators.TOTAL_ORDERS_COUNTER))

    @allure.step("Получить значение счётчика Выполнено за сегодня")
    def get_today_orders_counter(self):
        return int(self.get_text_from_element(OrdersPageLocators.TODAY_ORDERS_COUNTER))

    @allure.step("Получить список заказов в работе")
    def get_orders_in_work(self):
        elements = self.driver.find_elements(*OrdersPageLocators.ORDERS_IN_WORK)
        return [element.text.lstrip("0") for element in elements]

    @allure.step("Проверить, что номер заказа есть в разделе В работе")
    def is_order_number_in_work(self, order_number):
        order_number_locator = (
            OrdersPageLocators.ORDER_NUMBER_IN_WORK[0],
            OrdersPageLocators.ORDER_NUMBER_IN_WORK[1].format(order_number)
        )
        return self.find_visible_element(order_number_locator, timeout=20).is_displayed()
    
    @allure.step("Дождаться изменения счётчика Выполнено за всё время")
    def wait_for_total_orders_counter_changed(self, counter_before):
        return self.wait_for_number_to_be_greater_than(
            OrdersPageLocators.TOTAL_ORDERS_COUNTER,
            counter_before,
            timeout=30
        )


    @allure.step("Дождаться изменения счётчика Выполнено за сегодня")
    def wait_for_today_orders_counter_changed(self, counter_before):
        return self.wait_for_number_to_be_greater_than(
            OrdersPageLocators.TODAY_ORDERS_COUNTER,
            counter_before,
            timeout=30
        )
    
    @allure.step("Обновить страницу ленты заказов")
    def refresh_orders_page(self):
        self.refresh_page()