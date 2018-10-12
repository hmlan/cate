from selenium import webdriver
from selenium.webdriver.common.by import  By
from page.base_page import base
class HomePage(base):
    triangle=By.XPATH,"html/body/div/div/div[2]/div/div/div/div/div/i"
    selectcity=By.XPATH,"//div[text()='Auckland']"
    #searchbox=By.ID,"my-input"
    selectaddress=By.XPATH,"html/body/div/div/div/div/div/div[2]/div[5]/div[2]"
    def enterstorelist(self):
        #self.find_element(self.searchbox).send_keys("Auckland")
        self.find_element(self.triangle).click()
        self.find_element(self.selectcity).click()
        self.find_element(self.selectaddress).click()
