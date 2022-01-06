from selenium.webdriver import ActionChains
from browser_utils.src.waits import wait_for_page_to_load, wait_until_displayed, wait_until_not_displayed


@wait_for_page_to_load
def click_element(self, by_locator, x_offset=0, y_offset=0):
    element = self.driver.find_element(*by_locator)
    ActionChains(self.driver).move_to_element_with_offset(element, x_offset, y_offset).click().perform()

@wait_for_page_to_load
def click_and_drag_element(self, by_locator, x_destination, y_desitination):
    element = self.driver.find_element(*by_locator)
    ActionChains(self.driver).click_and_hold(element).move_by_offset(x_destination, y_desitination).perform()

@wait_for_page_to_load
def send_text_to_element(self, by_locator, text, clear_first=True, press_enter=False):
    if clear_first:
        self.__driver.find_element(*by_locator).clear()
    self.__driver.find_element(*by_locator).send_keys(text)
    if press_enter:
        self.__driver.find_element(*by_locator).send_keys(Keys.ENTER)

@wait_for_page_to_load
def hover_over_element(self, by_locator):
    element = self.__driver.find_element(*by_locator)
    ActionChains(self.__driver).move_to_element(element).perform()
