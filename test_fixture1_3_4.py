from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"

#(venv) PS C:\Projects_Python\silenium_auto_test> pytest -s test_fixture1_3_4.py


class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite 1..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("\nquit browser for test suite 1..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('\nstart test link 1')
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 1')
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("\nstart browser for test 2..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("\nquit browser for test 2..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('\nstart test link 2')
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('\nstart test basket 2')
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")