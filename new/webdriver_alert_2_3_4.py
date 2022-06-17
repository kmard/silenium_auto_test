import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:

    link ='https://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    butt = browser.find_element(By.CSS_SELECTOR,'[class="btn btn-primary"]')
    butt.click()

    alert = browser.switch_to.alert
    # alert.send_keys('text') # for text field
    # text = alert.text
    # alert.dismiss()
    alert.accept()

    x = browser.find_element(By.CSS_SELECTOR,'[id="input_value"]').text
    rez = math.log(abs(12*math.sin(int(x))))

    answer = browser.find_element(By.CSS_SELECTOR,'[id="answer"]')
    answer.send_keys(str(x))

    butSubmit = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.TAG_NAME,'button')))
    butSubmit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()