from PageObject_4_2_7.main_page import MainPage
import time

#pytest -s -v --tb=line --language=en test_main_page_4_2_7.py
#pytest -s -v --tb=line --language=ru test_main_page_4_2_7.py

def test_guest_can_go_to_login_page(browser):

    # link = "http://selenium1py.pythonanywhere.com/"
    # link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=midsummer'

    page = MainPage(browser, link)                  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                                     # открываем страницу
    page.choose_check_list('[name="language"]')     # find check-list and select language
    page.press_button('[class="btn btn-default"]')  # press bitton

    page.press_button('#login_link')          # выполняем метод страницы — переходим на страницу логина
    # time.sleep(5)