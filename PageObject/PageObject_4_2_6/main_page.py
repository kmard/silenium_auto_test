from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import Select


class MainPage(BasePage):

    def choose_check_list(self, path: str = ''):
        # assert self.is_element_present(By.CSS_SELECTOR,path)
        if self.is_element_present(By.CSS_SELECTOR,path):
            check_list = Select(self.browser.find_element(By.CSS_SELECTOR, path))
            check_list.select_by_value('es')


    def press_button(self, path: str = ''):
        # assert self.is_element_present(By.CSS_SELECTOR, path)
        if self.is_element_present(By.CSS_SELECTOR, path):
            login_link = self.browser.find_element(By.CSS_SELECTOR, path)
            login_link.click()




