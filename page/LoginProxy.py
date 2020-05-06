from page.LoginHandle import LoginHandle
from utils import DriverUtil


class LoginProxy():
    def __init__(self):
        self.loginhandle = LoginHandle()

    def login(self,username,password):
        self.loginhandle.input_username(username)
        self.loginhandle.input_password(password)
        self.loginhandle.click_subtton()

if __name__ == '__main__':
    driver = DriverUtil.get_driver()
    driver.get("http://www.yuetougu.com/")
    driver.find_element_by_id('ynLogin').click()

    # 对象库层
    loginproxy = LoginProxy()
    loginproxy.login('17600770073','Song826349794')