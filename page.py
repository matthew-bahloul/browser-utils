from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys


from waits import wait_for_page_to_load, wait_until_displayed, wait_until_not_displayed


class BasePage:
    def __init__(self, driver, wait_time=5):
        self.driver = driver
        self.driver.implicitly_wait(wait_time)

    def get_current_url(self):
        return self.driver.current_url

    def get_current_title(self):
        return self.driver.title

    def get_element_attribute(self, by_locator, attribute):
        return self.driver.find_element(*by_locator).get_attribute(attribute)

    def go_to_url(self, url):
        self.driver.get(url)

    def scroll_to_position_on_page(self, x_position, y_position):
        self.driver.execute_script(f'window.scrollTo({x_position}, {y_position})')
    
    def switch_to_tab(self, tab_position):
        self.driver.switch_to.window(self.driver.window_handles[tab_position])

    @wait_for_page_to_load
    def click_element(self, by_locator, x_offset=0, y_offset=0):
        element = self.driver.find_element(*by_locator)
        ActionChains(self.driver).move_to_element_with_offset(element, x_offset, y_offset).click().perform()

    @wait_for_page_to_load
    def click_and_drag_element(self, by_locator, x_destination, y_desitination):
        element = self.driver.find_element(*by_locator)
        ActionChains(self.driver).click_and_hold(element).move_by_offset(x_destination, y_desitination).perform()

    def get_elements(self, by_locator):
        return self.driver.find_elements(*by_locator)

    def get_element(self, by_locator):
        return self.get_elements(by_locator)[0]

    @wait_for_page_to_load
    def send_text_to_element(self, by_locator, text, clear_first=True, press_enter=False):
        if clear_first:
            self.driver.find_element(*by_locator).clear()
        self.driver.find_element(*by_locator).send_keys(text)
        if press_enter:
            self.driver.find_element(*by_locator).send_keys(Keys.ENTER)

    def hover_over_element(self, by_locator):
        element = self.driver.find_element(*by_locator)
        ActionChains(self.driver).move_to_element(element).perform()

