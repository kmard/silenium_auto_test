
# pytest -v --tb=line --language=en test_main_page_PageObject_4_1_7.py
#pytest -v --tb=line --language=ru test_main_page_PageObject_4_1_7.py

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    find_click_login_link(browser)

def find_click_login_link(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()