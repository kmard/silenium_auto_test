
# pytest test_3_3_3_pyTest.py


from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest



def test_Page1():


    link = "http://suninjuly.github.io/registration1.html"

    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.TAG_NAME, 'input')
    fill_elements(elements)


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text,'Registration failed registration1'

    # закрываем браузер после всех манипуляций
    browser.quit()


def test_Page2():


    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.TAG_NAME, 'input')
    fill_elements(elements)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text, 'Registration failed registration2'

    # закрываем браузер после всех манипуляций
    browser.quit()


def fill_elements(elements):
    for element in elements:
        if element.accessible_name == 'Input your first name':
            element.send_keys(element.accessible_name)
        elif element.accessible_name == 'Input your name':
            element.send_keys(element.accessible_name)
        elif element.accessible_name == 'Input your last name':
            element.send_keys(element.accessible_name)
        elif element.accessible_name == 'Input your email':
            element.send_keys(element.accessible_name)
        elif element.accessible_name == 'Input your phone:':
            element.send_keys(element.accessible_name)
        elif element.accessible_name == 'Input your address:':
            element.send_keys(element.accessible_name)


if __name__ == "__main__":
    pytest.main()





