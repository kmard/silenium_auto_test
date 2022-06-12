import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():

    # https://docs.pytest.org/en/latest/how-to/fixtures.html#adding-finalizers-directly
    # (venv) PS C:\Projects_Python\silenium_auto_test> pytest -s -v test_fixture_1_3_5_marks.py
    # После завершения теста, который вызывал фикстуру, выполнение фикстуры продолжится со строки,
    # следующей за строкой со словом yield
    # Для фикстур можно задавать область покрытия фикстур. Допустимые значения:
    # “function”, “class”, “module”, “session”.
    # Соответственно, фикстура будет вызываться один раз для тестового метода, один раз для класса,
    # один раз для модуля или один раз для всех тестов, запущенных в данной сессии.
    # :return:
    # browser


    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():


    def test_guest_should_see_login_link(self, browser):
        print('\n!!!pytest.mark.smoke')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")


    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print('\n!!!pytest.mark.regression')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")