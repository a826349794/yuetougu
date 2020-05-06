import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage
from utils import DriverUtil


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.username = (By.XPATH, '//*[@id="login"]/div/div/div[3]/form[2]/div[1]/input')
        self.password = (By.XPATH, '//*[@id="login"]/div/div/div[3]/form[2]/div[2]/input')
        self.subtton = (By.XPATH, '//*[@id="login"]/div/div/div[3]/form[2]/input')

    # 用户名输入
    def find_username(self):
        # return self.driver.find_element(self.username[0], self.username[1])
        return self.base_find_element(self.username)

    # 密码输入
    def find_password(self):
        # return self.driver.find_element(self.password[0], self.password[1])
        return self.base_find_element(self.password)

    # 登录按钮点击
    def find_subtton(self):
        # return self.driver.find_element(self.subtton[0], self.subtton[1])
        return self.base_find_element(self.subtton)


if __name__ == '__main__':
    driver = DriverUtil().get_driver()
    driver.get("http://www.yuetougu.com/")
    driver.find_element_by_id('ynLogin').click()

    loginpage = LoginPage()
    time.sleep(2)
    loginpage.find_username().send_keys('17600770073')
    loginpage.find_password().send_keys('Song826349794')
    loginpage.find_subtton().click()
