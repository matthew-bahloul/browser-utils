from browser_utils.common_actions import element_interactions, gets


class BasePage:
    def __init__(self, driver, wait_time=5):
        self.__driver = driver
        self.__driver_wait_time = wait_time
        self.__driver.implicitly_wait(self.__driver_wait_time)

    # common element interactions -----------------------------------------------
    click_element = element_interactions.click_element
    click_and_drag_element = element_interactions.click_and_drag_element
    hover_over_element = element_interactions.hover_over_element
    send_text_to_element = element_interactions.send_text_to_element

    # common gets 
    get_elements = gets.get_elements
    get_element = gets.get_element
    get_element_attribute = gets.get_element_attribute
    get_element_text = gets.get_element_text

    # browser-specific controls -----------------------------------------------
    def get_current_url(self):
        return self.__driver.current_url

    def get_current_title(self):
        return self.__driver.title

    def go_to_url(self, url):
        self.__driver.get(url)

    def refresh(self) -> None:
        self.__driver.refresh()

    def go_back(self) -> None:
        self.__driver.back()

    def go_forward(self) -> None:
        self.__driver.forward()

    def scroll_to_position_on_page(self, x_position, y_position):
        self.__driver.execute_script(f'window.scrollTo({x_position}, {y_position})')
    
    def switch_to_tab(self, tab_position):
        self.__driver.switch_to.window(self.__driver.window_handles[tab_position])

    def switch_to_frame(self, frame_reference=None):
        self.__driver.switch_to.frame(frame_reference) if frame_reference else self.__driver.switch_to.default_content()
