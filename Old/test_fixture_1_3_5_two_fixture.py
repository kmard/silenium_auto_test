import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():

    # https://docs.pytest.org/en/latest/how-to/fixtures.html#adding-finalizers-directly
    # (venv) PS C:\Projects_Python\silenium_auto_test> pytest -s -v test_fixture_1_3_5_two_fixture.py
    # После завершения теста, который вызывал фикстуру, выполнение фикстуры продолжится со строки,
    # следующей за строкой со словом yield
    #
    # Для фикстур можно задавать область покрытия фикстур. Допустимые значения:
    # “function”, “class”, “module”, “session”.
    # Соответственно, фикстура будет вызываться один раз для тестового метода, один раз для класса,
    # один раз для модуля или один раз для всех тестов, запущенных в данной сессии.
    #
    #При описании фикстуры можно указать дополнительный параметр autouse=True,
    # который укажет, что фикстуру нужно запустить для каждого теста даже без явного вызова:
    # :return:
    # browser


    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("\npreparing some critical data for every test")


class TestMainPage1():


    def test_guest_should_see_login_link(self, browser):
        print('\n!!!pytest.mark.smoke')
        # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")


    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print('\n!!!pytest.mark.regression')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")