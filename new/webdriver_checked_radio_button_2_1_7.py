from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:

    link ="http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    picture_treasure = browser.find_element(By.CSS_SELECTOR,'[id="treasure"]')
    x = picture_treasure.get_attribute('valuex')
    assert x is not None , 'picture_treasure is not have value'

    rez = math.log(abs(12 * math.sin(int(x))))

    input_answer = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    input_answer.send_keys(str(rez))

    checkbox = browser.find_element(By.CSS_SELECTOR,'[id="robotCheckbox"]')
    checkbox.click()

    radiobut = browser.find_element(By.CSS_SELECTOR,'[id="robotsRule"]')
    radiobut.click()

    time.sleep(1)

    buttonOk = browser.find_element(By.CSS_SELECTOR, "button.btn")
    buttonOk.click()

    #щем алерт
    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом алерта
    assert "Congrats, you've passed the task!"  in alert_text


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()