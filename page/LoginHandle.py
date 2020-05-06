from base.base_page import BaseHandle
from page.LoginPage import LoginPage
from utils import DriverUtil


class LoginHandle(BaseHandle):
    def __init__(self):
        self.loginpage = LoginPage()

    # 用户名输入
    def input_username(self,username):
        # self.loginpage.find_username().clear()
        # self.loginpage.find_username().send_keys(username)
        self.input_text(self.loginpage.find_username(),username)
    # 密码输入
    def input_password(self,password):
        # self.loginpage.find_password().clear()
        # self.loginpage.find_password().send_keys(password)
        self.input_text(self.loginpage.find_password(),password)
    # 登录按钮点击
    def click_subtton(self):
        self.loginpage.find_subtton().click()


if __name__ == '__main__':
    driver = DriverUtil().get_driver()
    driver.get("http://www.yuetougu.com/")
    driver.find_element_by_id('ynLogin').click()

    loginhandle = LoginHandle()
    loginhandle.input_username('17600770073')
    loginhandle.input_password('Song826349794')
    loginhandle.click_subtton()
