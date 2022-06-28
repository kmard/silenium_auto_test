from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, browser, url, timeout=2):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how: classmethod = By.CSS_SELECTOR, what: str = ''):
        try:
            self.browser.find_element(By.CSS_SELECTOR, what)
            return True
        except Exception as e:
            print(f'\nelement is not find {what}')
            return False
