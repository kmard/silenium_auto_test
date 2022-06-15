import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():

    # https://docs.pytest.org/en/latest/how-to/fixtures.html#adding-finalizers-directly
    #https://docs.pytest.org/en/latest/reference/reference.html?highlight=xfail#pytest.mark.xfail
    #
    #XFail: помечать тест как ожидаемо падающий
    #(venv) PS C:\Projects_Python\silenium_auto_test> pytest -v  test_fixture_1_3_5_marks_part3.py
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


class TestMainPage():
    # номер 1
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login(self, browser):
        print('номер 1')
        assert True

    # номер 2
    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self, browser):
        print('номер 2')
        assert True


class TestBasket():
    # номер 3
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page(self, browser):
        print('номер 3')
        assert True

    # номер 4
    @pytest.mark.smoke
    def test_guest_can_see_total_price(self, browser):
        print('номер 4')
        assert True


@pytest.mark.skip
class TestBookPage():
    # номер 5
    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket(self, browser):
        print('номер 5')
        assert True

    # номер 6
    @pytest.mark.regression
    def test_guest_can_see_book_price(self, browser):
        print('номер 6')
        assert True


# номер 7
@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue(browser):
    print('номер 7')
    assert True