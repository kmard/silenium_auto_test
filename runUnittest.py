import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def runRegistration(link):
    with webdriver.Chrome() as browser:
        browser.get(link)

        # short writing
        first_name_field = browser.find_element(By.CLASS_NAME, 'first').send_keys('Name1')
        # long writing
        # browser.find_element(By.CLASS_NAME, 'first')
        # first_name_field.click()
        # first_name_field.send_keys("Name")

        time.sleep(2)

#name mast start with Test
class TestFourPages(unittest.TestCase):

    #name mast start with Test
    def testFirstPage(self):
        runRegistration('http://suninjuly.github.io/registration1.html')

    # name mast start with Test
    def testSecondPage(self):
        print('testSecondPag')


if __name__ == '__main__':
    unittest.main()