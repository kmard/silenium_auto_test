from base_page import BasePage
from locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import  NoAlertPresentException
from math import log,sin

class MainPage(BasePage):

    def add_to_backed(self):
        batton_backet = self.browser.find_element(By.CSS_SELECTOR, '[value="Добавить в корзину"]')
        batton_backet.click()

    def solve_quiz_and_get_code(self):
        # field_enter = self.browser.find_element(By.CSS_SELECTOR, '[value="Добавить в корзину"]')
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        x = alert.text.split(" ")[2]
        answer = str(log(abs((12 * sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
