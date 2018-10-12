from appium import webdriver
import unittest
class First(unittest.TestCase):
# desired_capabilities = {
#             'platformName': 'Android',
#             'deviceName': '127.0.0.1:21503',
#             'platformVersion': '5.1.1',
#             'appPackage': 'com.saohuijia.bdt',
#             'appActivity': 'com.saohuijia.bdt.ui.activity.common.SplashActivity',
#             'newCommandTimeout': 3600,
#             'noReset': False,
#             #'fullReset':True,
#             'unicodeKeyboard': True,
#             'resetKeyboard': True}
# driver= webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
    def setUp(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '5.1.1'
        # 启动哪种设备，是真机还是模拟器？
        self.desired_caps['deviceName'] = 'Android Emulator'
        # 待测试的app的java package
        self.desired_caps['appPackage'] = 'com.saohuijia.bdt'
        # 待测试的app的Activity名字,注意，原生app的话要在activity前加个”.“。
        self.desired_caps['appActivity'] = 'com.saohuijia.bdt.ui.activity.common.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(10)
        # driver.find_element_by_id("com.saohuijia.bdt:id/item_index_menu_image").click()
    def tearDown(self):
        self.driver.quit()