from functools import wraps
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def wait_for_page_to_load(function):
    @wraps(function)
    def wrapper(self, *args, **kwargs):
        try:
            WebDriverWait(self.driver, 5).until(lambda _: self.driver.execute_script('return document.readyState') == 'complete')
        except Exception as e:
            pass
        function_call = function(self, *args, **kwargs)
        try:
            WebDriverWait(self.driver, 5).until(lambda _: self.driver.execute_script('return document.readyState') == 'complete')
        except Exception as e:
            pass
        return function_call
    return wrapper

def wait_until_displayed():
    pass


def wait_until_not_displayed():
    pass


