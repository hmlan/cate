from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
class base():
    def __init__(self, driver):
        self.driver = driver
    def find_element(self,locator):
        return self.driver.find_element(*locator)
    def find_elements(self,locator):
        return self.driver.find_elements(*locator)
    def wait(self, locator, time_out=10):
        wait_ = WebDriverWait(self.driver, time_out)
        wait_.until(lambda driver: driver.find_element(*locator))
