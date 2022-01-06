from browser_utils.common_actions import element_interactions, gets, booleans
from browser_utils.src import locator
from re import compile, search


def __get_locator_by_re(locators, pattern):
    pattern = compile(pattern) if type(pattern) is str else pattern
    return next((loc for loc in locators.__dict__ if search(loc, pattern)), None)


class BaseModal:
    def __init__(self, driver, wait_time=5):
        self._driver = driver
        self._driver_wait_time = wait_time
        self._driver.implicitly_wait(self._driver_wait_time)
        self.locators = locator.BaseLocator()
    
    # modal specific -----------------------------------------------
    def close(self):
        locator = __get_locator_by_re(self.locators, r'(close.*button|exit.*button)')
        if locator:
            element_interactions.click_element(locator)
        else:
            raise AttributeError('No locator for the close/exit button')
    exit = close

    def confirm(self):
        locator = __get_locator_by_re(self.locators, r'(confirm.*button|okay.*button)')
        if locator:
            element_interactions.click_element(locator)
        else:
            raise AttributeError('No locator for the confirm/okay button')
    okay = confirm

    def decline(self):
        locator = __get_locator_by_re(self.locators, r'(decline.*button|cancel.*button)')
        if locator:
            element_interactions.click_element(locator)
        else:
            raise AttributeError('No locator for the cancel/decline button')
    cancel = decline

    # common element interactions -----------------------------------------------
    click_element = element_interactions.click_element
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
    