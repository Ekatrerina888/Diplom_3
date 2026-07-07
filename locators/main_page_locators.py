from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[text()='Конструктор']"
    ORDERS_BUTTON = By.XPATH, "//p[text()='Лента Заказов']"
    LOGIN_BUTTON = By.XPATH, "//button[text()='Войти в аккаунт']"

    BUN_SECTION = By.XPATH, "//h2[text()='Булки']"
    FIRST_INGREDIENT = By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]"
    FIRST_INGREDIENT_COUNTER = By.XPATH, "(//p[contains(@class, 'counter_counter__num')])[1]"

    INGREDIENT_MODAL = By.XPATH, "//h2[text()='Детали ингредиента']"
    INGREDIENT_MODAL_CLOSE_BUTTON = By.XPATH, "//button[contains(@class, 'Modal_modal__close')]"

    BURGER_CONSTRUCTOR = By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]"
    ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"
    ORDER_MODAL = By.XPATH, "//div[contains(@class, 'Modal_modal')]"
    ORDER_NUMBER = By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow')]"
    ORDER_MODAL_CLOSE_BUTTON = By.XPATH, "//button[contains(@class, 'Modal_modal__close')]"
    MODAL_OVERLAY = By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]"