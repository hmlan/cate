from anriod.login import Login
from anriod.store import Store
from anriod.frist import First
import unittest
class teststore(First):
    """安卓本地超市测试"""
    def test_store_tuxdo_b(self):
        """超市的商品拼购详情开团测试"""
        login=Login(self.driver)
        login.login(13981401923,123456)
        store=Store(self.driver)
        store.tuxedo()
    def test_store_tuxdo_a(self):
        """超市的首页去开团测试"""
        login = Login(self.driver)
        login.login(13981401923,123456)
        store = Store(self.driver)
        store.tuxdo1()
    def test_store_buy(self):
        """超市的商品拼购详情直接购买测试"""
        login = Login(self.driver)
        login.login(13981401923, 123456)
        store = Store(self.driver)
        store.buy()
if __name__=="__main__":
    unittest.main()