import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

try:
    # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
    browser = webdriver.Chrome()

    # подготовка для теста
    # открываем страницу первого товара
    # данный сайт не существует, этот код приведен только для примера
    browser.get("https://fake-shop.com/book1.html")

    # добавляем товар в корзину
    add_button = browser.find_element(By.CSS_SELECTOR, ".add")
    add_button.click()

    # открываем страницу второго товара
    browser.get("https://fake-shop.com/book2.html")

    # добавляем товар в корзину
    add_button = browser.find_element(By.CSS_SELECTOR, ".add")
    add_button.click()

    # тестовый сценарий
    # открываем корзину
    browser.get("https://fake-shop.com/basket.html")

    # ищем все добавленные товары
    goods = browser.find_elements(By.CSS_SELECTOR, ".good")

    # проверяем, что количество товаров равно 2
    assert len(goods) == 2


finally:
    # После выполнения всех действий мы должны не забыть закрыть окно браузера
    browser.quit()
