from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from browser_utils.src.waits import wait_for_page_to_load, wait_until_displayed, wait_until_not_displayed


@wait_until_displayed
@wait_for_page_to_load
def click_element(self, by_locator, x_offset=0, y_offset=0):
    element = WebDriverWait(self._driver, self._driver_wait_time).until(EC.visibility_of_element_located(by_locator))
    
    chain = ActionChains(self._driver)
    if x_offset == 0 and y_offset == 0:
        chain.move_to_element(element).click()
    else:
        chain.move_to_element_with_offset(element, x_offset, y_offset).click()
    chain.perform()


@wait_until_displayed
@wait_for_page_to_load
def click_and_drag_element(self, by_locator, x_destination, y_desitination):
    element = WebDriverWait(self._driver, self._driver_wait_time).until(EC.visibility_of_element_located(by_locator))
    ActionChains(self._driver).click_and_hold(element).move_by_offset(x_destination, y_desitination).perform()


@wait_until_displayed
@wait_for_page_to_load
def send_text_to_element(self, by_locator, text, clear_first=True, press_enter=False):
    if clear_first:
        self._driver.find_element(*by_locator).clear()
    self._driver.find_element(*by_locator).send_keys(text)
    if press_enter:
        self._driver.find_element(*by_locator).send_keys(Keys.ENTER)


@wait_until_displayed
@wait_for_page_to_load
def hover_over_element(self, by_locator):
    element = self._driver.find_element(*by_locator)
    ActionChains(self._driver).move_to_element(element).perform()
