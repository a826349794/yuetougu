import time
import unittest

from utils import DriverUtil


class TestLogin(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    def setUp(self):
        self.driver.get("http://www.yuetougu.com/")

    def tearDown(self):
        time.sleep(2)

    def test_01_login(self):
        driver = self.driver
        # 业务操作 -- 元素定位和元素操作
        driver.find_element_by_xpath('//*[@id="login"]/div/div/div[3]/form[2]/div[1]/input').send_keys('17600770073')
        driver.find_element_by_xpath('//*[@id="login"]/div/div/div[3]/form[2]/div[2]/input').send_keys('Song826349794')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="login"]/div/div/div[3]/form[2]/input').click()
        time.sleep(3)
        msg1 = driver.find_element_by_xpath('//*[@id="topLink"]').text
        msg2 = driver.find_element_by_xpath('//*[@id="yn-header"]/div[1]/div/div[1]/span[1]').text
        self.assertIn('Xeon', msg1)
        print(msg2,msg1)
        driver.find_element_by_xpath('//*[@id="ynLogout"]').click()
