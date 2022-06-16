from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""
docs
https://docs.python.org/3/library/os.path.html
"""

try:

    link ='https://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR,'[name="firstname"]')
    first_name.send_keys('first_name')

    second_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    second_name.send_keys('second_name')

    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    email.send_keys('email')

    # import os
    #
    # current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    # file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    # element.send_keys(file_path)

    load_File = browser.find_element(By.CSS_SELECTOR,'[id="file"]')
    load_File.send_keys(r'C:\Users\ПК\Documents\новый 2.txt')

    butSubmit = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
    butSubmit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()