from browser_utils.src.waits import wait_for_page_to_load, wait_until_displayed


@wait_until_displayed
@wait_for_page_to_load
def has_attribute(self, by_locator, attribute):
    return self._driver.find_element(*by_locator).get_attribute(attribute) != ''


@wait_until_displayed
@wait_for_page_to_load
def has_text(self, by_locator, text, is_case_sensitive=False):
    element_text = self._driver.find_element(*by_locator)

    if is_case_sensitive:
        return element_text == text
    return element_text.lower() == text.lower()


@wait_for_page_to_load
def is_visible(self, by_locator):
    try:
        el = self.driver.find_element(*by_locator)
        return el.is_displayed()
    except Exception:
        return False
