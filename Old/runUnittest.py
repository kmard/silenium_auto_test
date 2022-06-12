import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def runRegistration(link, self, numberPage):
    with webdriver.Chrome() as browser:
        browser.get(link)

        # short writing
        first_name_field = browser.find_element(By.CLASS_NAME, 'first').send_keys('Name1')
        # long writing
        # browser.find_element(By.CLASS_NAME, 'first')
        # first_name_field.click()
        # first_name_field.send_keys("Name")

        second_name_field = browser.find_element(By.CLASS_NAME, "second").send_keys('Second2')

        email_field = browser.find_element(By.CLASS_NAME, "third").send_keys('email@domain.com')

        if numberPage == 1:
            phone_field = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your phone:"]').send_keys('+7900000000')
        else:
            # for next pages
            phone_field = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your phone:"]').send_keys('+7900000000')
            # time.sleep(100)

        # button registration
        button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        #wait for registration and refresh  welcome_text
        time.sleep(1)

        #recieve text message
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text

        self.assertEqual(welcome_text,'Congratulations! You have successfully registered!','welcome_text texts are different')

        # time.sleep(10)

#name mast start with Test
class TestFourPages(unittest.TestCase):

    #name mast start with Test
    def testFirstPage(self):
        runRegistration('http://suninjuly.github.io/registration1.html',self,1)

    # name mast start with Test
    def testSecondPage(self):
        runRegistration('http://suninjuly.github.io/registration2.html',self,2)


if __name__ == '__main__':
    unittest.main()