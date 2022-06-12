import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    """
    docs https://docs.pytest.org/en/latest/reference/reference.html?highlight=fixture#pytest.fixture
    (venv) PS C:\Projects_Python\silenium_auto_test> pytest -s -v test_fixture_1_3_5_simple.py
    :return:
    instanse browser
    """
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    return browser


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print('\n call test_guest_should_see_login_link')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print('\n call test_guest_should_see_basket_link_on_the_main_page')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")