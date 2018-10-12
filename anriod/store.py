from selenium.webdriver.common.by import By
from page.base_page import base
from time import sleep
class Store(base):
    home=By.ID,"com.saohuijia.bdt:id/main_image_news"
    locatingcity=By.ID,"com.saohuijia.bdt:id/index_action_left"
    selectcity=By.XPATH,"//android.widget.TextView[contains(@text,'Auckland City')]"
    localsupermarket=By.ID,"com.saohuijia.bdt:id/item_index_menu_linear"
    selectshop=By.ID,"com.saohuijia.bdt:id/text_merchant_name"
    more=By.XPATH,"//android.widget.TextView[contains(@text,'更多')]"
    tostartgroup=By.CLASS_NAME,"android.widget.Button"#定位多个元素
    selecttime=By.ID,"com.saohuijia.bdt:id/text_submit_selecttime"
    selectdate=By.CLASS_NAME,"android.widget.RadioButton"#定位了多个元素
    selecthour=By.XPATH,"//android.widget.RadioButton[contains(@text,'02:00~03:00')]"
    remarks=By.ID,"com.saohuijia.bdt:id/text_submit_orderComment"
    addremarks=By.ID,"com.saohuijia.bdt:id/edit_comment_content"
    finish=By.ID,"com.saohuijia.bdt:id/btn_finished"
    submit=By.ID,"com.saohuijia.bdt:id/submit_order_button_submit"

    productimage=By.XPATH,"//android.widget.TextView[contains(@text,'杯子 222')]"#定位多个元素
    minegroup=By.ID,"com.saohuijia.bdt:id/linear_collage_buy"
    singbuy=By.ID,"com.saohuijia.bdt:id/linear_single_buy"
    payway=By.ID,"com.saohuijia.bdt:id/text_submit_payway"
    paycash=By.ID,"com.saohuijia.bdt:id/item_pay_type_cash"
    def tuxedo(self):
        self.find_element(self.home).click()
        self.find_element(self.locatingcity).click()
        self.find_element(self.selectcity).click()
        self.find_elements(self.localsupermarket)[6].click()
        sleep(5)
        self.find_element(self.more).click()
        self.find_elements(self.tostartgroup)[0].click()
        self.find_element(self.selecttime).click()
        self.find_elements(self.selectdate)[1].click()
        self.find_element(self.selecthour).click()
        self.find_element(self.remarks).click()
        self.find_element(self.addremarks).send_keys(123)
        sleep(5)
        self.find_element(self.finish).click()
        self.find_element(self.submit).click()
    def tuxdo1(self):
        self.find_element(self.home).click()
        self.find_element(self.locatingcity).click()
        self.find_element(self.selectcity).click()
        self.find_elements(self.localsupermarket)[6].click()
        sleep(2)
        self.find_element(self.productimage).click()
        self.find_element(self.minegroup).click()
        self.find_element(self.selecttime).click()
        self.find_elements(self.selectdate)[1].click()
        self.find_element(self.selecthour).click()
        self.find_element(self.submit).click()
    def buy(self):
        self.find_element(self.home).click()
        self.find_element(self.locatingcity).click()
        self.find_element(self.selectcity).click()
        self.find_elements(self.localsupermarket)[6].click()
        self.find_element(self.productimage).click()
        self.find_element(self.singbuy).click()
        self.find_element(self.payway).click()
        self.find_element(self.paycash).click()
        self.find_element(self.selecttime).click()
        self.find_elements(self.selectdate)[1].click()
        self.find_element(self.selecthour).click()
        self.find_element(self.submit).click()