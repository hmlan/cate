from page.base_page import base
from selenium.webdriver.common.by import By
import time
class TakeawayPage(base):
    shopname=By.XPATH,"html/body/div/div/div[3]/div[2]/div/div[5]"
    shoppingbutton1=By.ID,"1015150"
    shoppingbutton2=By.ID,"30574926285"
    shoppingbutton2_=By.XPATH,"//div[text()='加入购物车']"
    settlementbutton=By.CSS_SELECTOR,".flex-row.align-items-center.justify-content-center.shj-background-color-pink.shj-color-white.shj-cursor-hand.shj-width-100"
    def entershop(self):
        # self.wait(self.shopname)
        self.find_element(self.shopname).click()
        # self.wait(self.shoppingbutton1)
        self.find_element(self.shoppingbutton1).click()
        # self.wait(self.shoppingbutton2)
        self.find_element(self.shoppingbutton2).click()
        #self.wait(self.shoppingbutton2_)
        self.js="window.scrollTo(590,918);"
        self.driver.execute_script(self.js)
        self.find_element(self.shoppingbutton2_).click()
        # self.wait(self.settlementbutton)
        self.js1="window.scrollTo(0,250);"
        self.driver.execute_script(self.js1)
        time.sleep(5)
        self.find_element(self.settlementbutton).click()

