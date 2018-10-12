from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from page.base_page import base
class LoginPage(base):
    # def __init__(self,driver):
    #     self.driver=driver
    # def find_element(self,locator):
    #     return self.driver.find_element(*locator)
    loginbutton=By.XPATH,"html/body/div/div/div[2]/div/div/div[2]/ul/li[1]"
    username=By.XPATH,"//input[@placeholder='请输入手机号']"
    password=By.XPATH,"//input[@placeholder='请输入6 ~ 12位密码']"
    loginbutton1=By.XPATH,"//div[text()='登录']"
    English_text=By.XPATH,"//li[text()='English']"
    #logout=By.XPATH,"html/div/div/div/div/div[2]/ul/li"
    def userlogin(self,username,password):
        self.find_element(self.loginbutton).click()
        self.find_element(self.username).send_keys(username)
        self.find_element(self.password).send_keys(password)
        self.find_element(self.loginbutton1).click()
    def find_English(self):
        return self.find_element(self.English_text).text