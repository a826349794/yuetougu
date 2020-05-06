import time
import unittest

from utils import DriverUtil


class Test_username(unittest.TestCase):
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

    def test_02_username_error(self):
        driver = self.driver
        # 业务操作 -- 元素定位和元素操作
        driver.find_element_by_id('ynLogin').click()
        driver.find_element_by_xpath('//*[@id="login"]/div/div/div[3]/form[2]/div[1]/input').send_keys('17600770076')
        driver.find_element_by_xpath('//*[@id="login"]/div/div/div[3]/form[2]/div[2]/input').send_keys('Song826349794')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="login"]/div/div/div[3]/form[2]/input').click()
        msg = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/span").text
        print('提示信息:',msg)
        # 断言提示信息
        self.assertIn("手机号不存在", msg)
