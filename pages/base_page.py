from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located(locator)
        )

    def find_visible_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def find_clickable_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    def click_on_element(self, locator):
        element = self.find_clickable_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    def set_text_to_element(self, locator, text):
        element = self.find_visible_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_visible_element(locator).text

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url_contains(self, url_part, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.url_contains(url_part)
        )

    def wait_for_visibility_of_element(self, locator, timeout=10):
        return self.find_visible_element(locator, timeout)

    def wait_for_invisibility_of_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.invisibility_of_element_located(locator)
        )

    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_visible_element(source_locator)
        target = self.find_visible_element(target_locator)

        self.driver.execute_script("arguments[0].scrollIntoView();", source)

        actions = ActionChains(self.driver)
        actions.click_and_hold(source).pause(1)
        actions.move_to_element(target).pause(1)
        actions.release().perform()

    def wait_for_overlay_disappear(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.invisibility_of_element_located(locator)
        )

    def drag_and_drop_with_js(self, source_locator, target_locator):
        source = self.find_visible_element(source_locator)
        target = self.find_visible_element(target_locator)

        script = """
        const source = arguments[0];
        const target = arguments[1];

        const dataTransfer = new DataTransfer();

        source.dispatchEvent(new DragEvent('dragstart', {
            bubbles: true,
            cancelable: true,
            dataTransfer
        }));

        target.dispatchEvent(new DragEvent('drop', {
            bubbles: true,
            cancelable: true,
            dataTransfer
        }));

        source.dispatchEvent(new DragEvent('dragend', {
            bubbles: true,
            cancelable: true,
            dataTransfer
        }));
    """

        self.driver.execute_script(script, source, target)

    def wait_for_text_not_in_element(self, locator, text, timeout=20):
        return WebDriverWait(self.driver, timeout).until_not(
            expected_conditions.text_to_be_present_in_element(locator, text)
        )
    
    def wait_for_number_to_be_greater_than(self, locator, number, timeout=30):
        def number_is_greater_than(driver):
            element_text = driver.find_element(*locator).text
            return int(element_text) > number

        return WebDriverWait(self.driver, timeout).until(number_is_greater_than)
    
    def refresh_page(self):
        self.driver.refresh()