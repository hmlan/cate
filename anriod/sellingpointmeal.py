from appium import webdriver
from selenium.webdriver.common.by import By
from page.base_page import base
class SellingPointMeal(base):
    selling=By.ID,"com.saohuijia.bdt:id/item_index_menu_linear"
    def clicksell(self):
        self.find_element(self.selling).click()