# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('http://suninjuly.github.io/simple_form_find_task.html')
# button = browser.find_element('submit_button')
#
# from selenium import webdriver
# from selenium.webdriver.common.by import  By
#
# browser = webdriver.Chrome()
# browser.get('http://suninjuly.github.io/simple_form_find_task.html')
# button = browser.find_element(By.ID,'submit_button')
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = 'http://suninjuly.github.io/simple_form_find_task.html'
# broweser= webdriver.Chrome()
# broweser.get(link)
# button = broweser.find_element(By.ID,'submit_button')
#
# broweser.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.ID, "submit_button")
#     button.click()
#
# finally:
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.NAME,'first_name')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME,'last_name')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.NAME,'firstname')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID,'country')
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR,"button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
# link = "http://suninjuly.github.io/find_link_text"
#
# seek_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     link_seek = browser.find_element(By.LINK_TEXT,seek_text)
#     link_seek.click()
#
#
#     input1 = browser.find_element(By.NAME,'first_name')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME,'last_name')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.NAME,'firstname')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID,'country')
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR,"button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.TAG_NAME,'input')
#     [elements[i].send_keys('Мой ответ {}'.format(i)) for i in range(len(elements))]
#
#     button = browser.find_element(By.CSS_SELECTOR,"button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "https://suninjuly.github.io/find_xpath_form"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.NAME,'first_name')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME,'last_name')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.NAME,'firstname')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID,'country')
#     input4.send_keys("Russia")
#     button = browser.find_element(By.XPATH,"/html/body/div/form/div[6]/button[3]")
#     # button = browser.find_element_by_xpath('//button[@type="submit"]')
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла

# //
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    firstName = browser.find_element(By.XPATH,'/html/body/div/form/div[1]/div[1]/input')
    firstName.send_keys('First1')

    lastName = browser.find_element(By.XPATH,'/html/body/div/form/div[1]/div[2]/input')
    lastName.send_keys('Last name')

    email = browser.find_element(By.XPATH,'/html/body/div/form/div[1]/div[3]/input')
    email.send_keys('email@google.com')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME,"h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

























