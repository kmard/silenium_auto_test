
from selenium.common.exceptions import TimeoutException

class BasePage():

    def __init__(self, browser, url: str, timeout: int = 2):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (TimeoutException):
            return False
        return True