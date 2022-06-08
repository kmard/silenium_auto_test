from main_page_backet import MainPage
from init_backet import *



def test_guest_can_go_to_backet_page(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                       # открываем страницу
    page.add_to_backed()             # выполняем метод страницы - add to backet
    page.solve_quiz_and_get_code()    # work with modal window