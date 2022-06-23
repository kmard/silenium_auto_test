
# pytest -s -v test_3_5_4_fixture_marks_skip.py


# Как же регистрировать метки?
#
# Создайте файл pytest.ini в корневой директории вашего тестового проекта и добавьте в файл следующие строки:
#
# [pytest]
# markers =
#     smoke: marker for smoke tests
#     regression: marker for regression tests


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


# function”, “class”, “module”, “session”.
@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

# @pytest.fixture(autouse=True)
# def prepare_data():
#     print()
#     print("preparing some critical data for every test")


class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    @pytest.mark.skip
    def test_guest_should_see_login_link(self, browser):
        print("\nstart test1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")


    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("\nstart test2")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")

