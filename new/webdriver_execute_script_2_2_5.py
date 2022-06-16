from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

"""
docs
https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView
"""

try:

    link ='https://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    browser.execute_script("alert('Robots at work');")
    # browser.execute_script("document.title='Script executing';")
    # browser.execute_script("document.title='Script executing';alert('Robots at work');")

    # #щем алерт
    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()

    x = browser.find_element(By.CSS_SELECTOR,'[id="input_value"]').text
    input_answer = browser.find_element(By.CSS_SELECTOR,'[id="answer"]')

    rez = math.log(abs(12 * math.sin(int(x))))
    input_answer.send_keys(str(rez))

    checkbox = browser.find_element(By.CSS_SELECTOR, '[id="robotCheckbox"]')
    checkbox.click()

    radiobut = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
    rez = radiobut.location_once_scrolled_into_view
    radiobut.click()


    button = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
    rez =button.location_once_scrolled_into_view
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()