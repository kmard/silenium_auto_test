import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

#name mast start with Test
class TestFourPages(unittest.TestCase):

    #name mast start with Test
    def testFirstPage(self):
        print('testFirstPage')

    # name mast start with Test
    def testSecondPage(self):
        print('testSecondPag')


if __name__ == '__main__':
    unittest.main()