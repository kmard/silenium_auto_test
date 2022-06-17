import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:

    link ='http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    butt = browser.find_element(By.CSS_SELECTOR,'[class="trollface btn btn-primary"]')
    butt.click()

    new_window = browser.window_handles[1]
    current_window = browser.current_window_handle
    browser.switch_to.window(new_window)


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