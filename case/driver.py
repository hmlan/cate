from selenium import webdriver
import unittest
class mytest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://172.18.0.50:9009")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()