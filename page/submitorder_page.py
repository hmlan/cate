from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from page.base_page import base
import time
class SubmitorderPage(base):
    trigon1=By.CSS_SELECTOR,".el-button.el-button--default.el-button--medium.el-dropdown__caret-button"
    #class类名不允许符合类名做参数,及中间有空格类名
    #trigon1=By.CSS_SELECTOR,".el-dropdown__icon.el-icon-arrow-down"
    #address=By.XPATH,"//b[text()='haha']"
    address=By.XPATH,"html/body/ul/li[4]"
    selectdate=By.XPATH,"//span[text()='选择时间']"
    selectmouth=By.XPATH,"html/body/ul[2]/li[2]"
    selectime=By.XPATH,"html/body/ul[3]/li[4]/span"
    trigon2=By.XPATH,"html/body/div/div/div[3]/div/div[2]/div[3]/div/div[3]/div/div[2]/div/div/button[2]/span/i"
    trigon3=By.XPATH,"html/body/div/div/div[3]/div/div[2]/div[3]/div/div[3]/div/div[2]/div[2]/div/button[2]/span/i"
    payment=By.XPATH,"//span[text()='立即付款']"
    invite=By.XPATH,"//li[text()='自取']"
    alipay=By.XPATH,"html/body/div/div/div[3]/div/div/[2]/div[3]/div/div[2]/div/div/p"
    wechat=By.XPATH,"html/body/div/div/div[3]/div/div/[2]/div[3]/div/div[2]/div/div[2]/p"
    nzd=By.XPATH,"html/body/div/div/div[3]/div/div/[2]/div[3]/div/div[2]/div/div[3]/p"
    paymentway=[alipay,wechat,nzd]
    def submit(self):
        # 当你调用ActionChains的方法时，不会立即执行，而是会将所有的操作按顺序存放在一个队列里，当你调用perform()方法时，队列中的时间会依次执行。
        #action=ActionChains(self.driver)
        #trigon1_=self.find_elements(self.trigon1)[0]
        ActionChains(self.driver).move_to_element(self.find_element(self.trigon1)).perform()
        time.sleep(5)
        self.find_element(self.address).click()
        time.sleep(3)
        # self.find_element(self.address).click()
        #self.find_element(a).click()
        self.find_element(self.selectdate).click()
        ActionChains(self.driver).move_to_element(self.find_element(self.trigon2)).perform()
        time.sleep(5)
        self.find_element(self.selectmouth).click()
        ActionChains(self.driver).move_to_element(self.find_element(self.trigon3)).perform()
        time.sleep(5)
        self.find_element(self.selectime).click()
        self.find_element(self.payment).click()
    # def invite(self):
    #     self.find_element(self.invite).click()




