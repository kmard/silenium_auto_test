import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

#документация по выводу данных в консоль вывода
# https://docs.pytest.org/en/stable/how-to/usage.html#modifying-python-traceback-printing

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


class TestMainPages():

    def test_guest_should_see_login_link(self, browser):
        rez = ''
        ml = [
            'https://stepik.org/lesson/236895/step/1',
            'https://stepik.org/lesson/236896/step/1',
            'https://stepik.org/lesson/236897/step/1',
            'https://stepik.org/lesson/236898/step/1',
            'https://stepik.org/lesson/236899/step/1',
            'https://stepik.org/lesson/236903/step/1',
            'https://stepik.org/lesson/236904/step/1',
            'https://stepik.org/lesson/236905/step/1']

        for i in ml:
            browser.get(i)
            browser.implicitly_wait(10)
            try:
                answer = ''
                field_enter = browser.find_element(By.TAG_NAME,'textarea')
                field_enter.send_keys(str(math.log(int(time.time()))))
                button = browser.find_element(By.CSS_SELECTOR, '[class="submit-submission"]').click()

                field_answer = None
                field_answer = WebDriverWait(browser,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="smart-hints__hint"]')))

                if field_answer != None:
                    answer = field_answer.text

                if answer != '' and answer != 'Correct!':
                    rez += str(answer)
            except Exception as e:
                print(e, type(e))
                continue


        print(f'\n Aswer: {rez}')