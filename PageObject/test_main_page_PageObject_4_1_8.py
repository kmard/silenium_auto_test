
# pytest -v --tb=line --language=en test_main_page_PageObject_4_1_8.py
#pytest -v --tb=line --language=ru test_main_page_PageObject_4_1_8.py

from selenium.webdriver.common.by import By
import time


def test_add_to_cart(browser):
     ProductPage(browser,url='https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/')
     find_click_buttton_find(browser)

def ProductPage(browser,url):
      return browser.get(url)

def find_click_buttton_find(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, '[value="Найти"]')
    login_link.click()
    # time.sleep(10)