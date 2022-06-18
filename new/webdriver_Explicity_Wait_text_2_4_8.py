import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    browser = webdriver.Chrome()

    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    # Ждем цену прайса в 100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[id="price"]'), '100')
    )

    btn = browser.find_element(By.CSS_SELECTOR, '[id="book"]')
    btn.click()

    x = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]').text
    rez = math.log(abs(12 * math.sin(int(x))))

    answer = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    answer.send_keys(rez)

    sub = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    sub.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()