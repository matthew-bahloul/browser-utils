from browser_utils.src.waits import wait_for_page_to_load, wait_until_displayed, wait_until_not_displayed

@wait_until_displayed
def get_elements(self, by_locator):
    return self.__driver.find_elements(*by_locator)

@wait_until_displayed
def get_element(self, by_locator):
    res = self.get_elements(by_locator)[0]
    return res if res else None

@wait_until_displayed
def get_element_attribute(self, by_locator, attribute):
    return self.__driver.find_element(*by_locator).get_attribute(attribute)

@wait_until_displayed
def get_element_text(self, by_locator):
    return self.__driver.find_element(*by_locator).text
