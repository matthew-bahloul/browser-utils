from browser_utils.common_actions import element_interactions, gets, booleans
from browser_utils.src import locator


class BaseComponent:
    def __init__(self, driver, wait_time=5):
        self._driver = driver
        self._driver_wait_time = wait_time
        self._driver.implicitly_wait(self._driver_wait_time)
        self.locators = locator.BaseLocator()
    
    # common element interactions -----------------------------------------------
    click_element = element_interactions.click_element
    click_and_drag_element_by_offset = element_interactions.click_and_drag_element_by_offset
    click_and_drag_element = element_interactions.click_and_drag_element
    hover_over_element = element_interactions.hover_over_element
    send_text_to_element = element_interactions.send_text_to_element

    # common gets -----------------------------------------------
    get_elements = gets.get_elements
    get_element = gets.get_element
    get_element_attribute = gets.get_element_attribute
    get_element_text = gets.get_element_text
    
    # common booleans -----------------------------------------------
    has_attribute = booleans.has_attribute
    has_text = booleans.has_text
    is_visible = booleans.is_visible
    