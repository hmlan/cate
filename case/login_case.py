from selenium import webdriver
from case.driver import mytest
from page.login_page import LoginPage
from page.home_page import HomePage
from page.takeaway_page import TakeawayPage
from page.submitorder_page import SubmitorderPage
from selenium.webdriver.common.by import By
class testlogin(mytest):




    def test_login(self):
        """美食pc的流程测试"""
        loginpage=LoginPage(self.driver)
        loginpage.userlogin('13981401923','123456')
        self.assertEqual(loginpage.find_English(),'English')
        homepage=HomePage(self.driver)
        homepage.enterstorelist()
        takeawaypage=TakeawayPage(self.driver)
        takeawaypage.entershop()
        submitorderpage=SubmitorderPage(self.driver)
        submitorderpage.submit()




