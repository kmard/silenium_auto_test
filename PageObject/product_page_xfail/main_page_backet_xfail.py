
from selenium.webdriver.common.by import By
from selenium.common.exceptions import  NoAlertPresentException
from math import log,sin
from base_page_xfail import BasePage

class MainPage(BasePage):

    def add_to_backed(self):
        batton_backet = self.browser.find_element(By.CSS_SELECTOR, '[value="Добавить в корзину"]')
        batton_backet.click()

    def should_be_present_in_cart(self) -> None:

        assert self.is_element_present(
            By.CSS_SELECTOR, "div.alertinner"
        ), "No alert that a product has been added to cart"
        alert_text = self.browser.find_element(
            By.XPATH, '//*[@id="messages"]/div[1]/div').text
        product_name = self.browser.find_element(
            By.TAG_NAME, "h1").text
        assert alert_text.find(product_name) !=-1, \
            f"The alert contains wrong product name: {alert_text} - {product_name}"


    def solve_quiz_and_get_code(self):
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
