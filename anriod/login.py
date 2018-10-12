from selenium.webdriver.common.by import By
from page.base_page import base
class Login(base):
    mine=By.ID,"com.saohuijia.bdt:id/main_image_mine"
    fastlogin=By.ID,"com.saohuijia.bdt:id/mine_home_image_head"
    phoneinput=By.ID,"com.saohuijia.bdt:id/edit_phone"
    passwordinput=By.ID,"com.saohuijia.bdt:id/edit_password"
    loginbutton=By.ID,"com.saohuijia.bdt:id/auth_btn_login"
    def login(self,phone,password):
        self.find_element(self.mine).click()
        self.find_element(self.fastlogin).click()
        self.find_element(self.phoneinput).send_keys(phone)
        self.find_element(self.passwordinput).send_keys(password)
        self.find_element(self.loginbutton).click()