from base_page import BasePage
from locators import MainPageLocators

class MainPage(BasePage):

    def go_to_login_page(self):
        # login_link = self.browser.find_element(By.CSS_SELECTOR, *MainPageLocators.LOGIN_LINK)
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    # not use
    def should_be_login_link(self):
       assert self.browser.find_element(*MainPageLocators.LOGIN_LINK)  #"Login link is not presented"