from browser_utils.common_actions import element_interactions, gets
from browser_utils.src import locator


class BaseComponent:
    def __init__(self, driver, wait_time=5):
        self.__driver = driver
        self.__driver_wait_time = wait_time
        self.__driver.implicitly_wait(self.__driver_wait_time)
        self.locators = locator.BaseLocator()
    
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
    