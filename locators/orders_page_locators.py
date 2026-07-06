from selenium.webdriver.common.by import By


class OrdersPageLocators:
    ORDERS_HEADER = By.XPATH, "//h1[text()='Лента заказов']"

    TOTAL_ORDERS_COUNTER = By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"
    TODAY_ORDERS_COUNTER = By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"

    ORDERS_IN_WORK = By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'text_type_digits-default')]"
    ORDER_NUMBER_IN_FEED = By.XPATH, "//p[contains(@class, 'text_type_digits-default')]"
    ORDER_NUMBER_IN_WORK = By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[text()='{}']"