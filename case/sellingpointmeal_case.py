import unittest
from appium import webdriver
from anriod.sellingpointmeal import SellingPointMeal
from anriod.frist import First
class testsellingpointmeal(First):
    # def setUp(self):
    #     self.desired_caps = {}
    #     self.desired_caps['platformName'] = 'Android'
    #     self.desired_caps['platformVersion'] = '5.1.1'
    #     # 启动哪种设备，是真机还是模拟器？
    #     self.desired_caps['deviceName'] = 'Android Emulator'
    #     # 待测试的app的java package
    #     self.desired_caps['appPackage'] = 'com.saohuijia.bdt'
    #     # 待测试的app的Activity名字,注意，原生app的话要在activity前加个”.“。
    #     self.desired_caps['appActivity'] = 'com.saohuijia.bdt.ui.activity.common.SplashActivity'
    #     self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
    #     # driver.find_element_by_id("com.saohuijia.bdt:id/item_index_menu_image").click()
    def test_sellingpointmeal(self):
        """安卓的美食外卖流程测试"""
        sellingpointmeal=SellingPointMeal(self.driver)
        sellingpointmeal.clicksell()