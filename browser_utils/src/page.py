from browser_utils.common_actions import element_interactions, gets, booleans


class BasePage:
    def __init__(self, driver, wait_time=5):
        self._driver = driver
        self._driver_wait_time = wait_time
        self._driver.implicitly_wait(self._driver_wait_time)

    # browser-specific controls -----------------------------------------------
    def get_current_url(self):
        return self._driver.current_url

    def get_current_title(self):
        return self._driver.title

    def go_to_url(self, url):
        self._driver.get(url)

    def refresh(self) -> None:
        self._driver.refresh()

    def go_back(self) -> None:
        self._driver.back()

    def go_forward(self) -> None:
        self._driver.forward()

    def scroll_to_position_on_page(self, x_position, y_position):
        self._driver.execute_script(f'window.scrollTo({x_position}, {y_position})')
    
    def switch_to_tab(self, tab_position):
        self._driver.switch_to.window(self._driver.window_handles[tab_position])

    def switch_to_frame(self, frame_reference=None):
        self._driver.switch_to.frame(frame_reference) if frame_reference else self._driver.switch_to.default_content()

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
    