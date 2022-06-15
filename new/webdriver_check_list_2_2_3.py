from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:

    link ='http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR,'[id="num1"]').text
    num2 = browser.find_element(By.CSS_SELECTOR, '[id="num2"]').text
    sum = int(num1)+int(num2)

    list = Select(browser.find_element(By.CSS_SELECTOR, '[id="dropdown"]'))
    list.select_by_value(str(sum))             #select_by_visible_text()

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