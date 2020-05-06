import json
import time
import unittest
from parameterized import parameterized
from page.LoginProxy import LoginProxy
from utils import DriverUtil, get_tips_msg

def read_data():
    with open("../data/login.json","r",encoding="utf-8")as f:
        data = json.load(f)
    return data
# def read_data2():
#     with open("../data/login_error.json","r",encoding="utf-8")as f:
#         data2 = json.load(f)
#     return data2


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
        self.driver.find_element_by_id('ynLogin').click()

        self.loginproxy = LoginProxy()

    def tearDown(self):
        time.sleep(2)
    @parameterized.expand(read_data)
    def test_01_login(self,username,password,yuqi):
        driver = self.driver

        # 调用业务层输入
        self.loginproxy.login(username,password)

        msg1 = driver.find_element_by_xpath('//*[@id="yn-header"]/div[1]/div/div[1]/span[1]').text
        msg2 = driver.find_element_by_xpath('//*[@id="topLink"]').text
        self.assertIn(yuqi, msg2)
        print(msg1, msg2)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ynLogout"]').click()

    # @parameterized.expand(read_data2)
    def test_02_username_error(self,username,password,yuqi):
        time.sleep(2)
        # 调用业务层输入
        self.loginproxy.login(username,password)

        msg = get_tips_msg()
        print('提示信息:', msg)
        self.assertIn(yuqi, msg)

    # @parameterized.expand(read_data)
    def test_03_password_error(self,username,password,yuqi):
        # 调用业务层输入
        self.loginproxy.login(username,password)

        msg = get_tips_msg()
        print('提示信息;', msg)
        self.assertIn(yuqi, msg)
