# 创建一个类用于保存 / 获取/ 销毁 浏览器驱动对象
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class DriverUtil:
    driver = None
    #定义一个方法，获取浏览器对象
    @classmethod
    def get_driver(cls):
        #如果需要返回浏览器--类属性driver中得到驱动对象
        #如果driver总没有驱动对象的话None-->先创建浏览器驱动对线下 赋值给driver
        if cls.driver is None:
            #创建浏览器驱动对象，赋值给driver
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)

        return cls.driver
    @classmethod
    def quit_driver(cls):
        #如果类属性driver中没有驱动对象的时候--> 不需要退出
        #当类属性driver中有驱动对象的时候---需要退出
        if cls.driver is not None:
            cls.driver.quit()
            cls.driver = None

def get_tips_msg():
    #登录提示信息
    time.sleep(2)
    msg = DriverUtil.get_driver().find_element_by_xpath("/html/body/div[3]/div/div/div[2]/span").text
    return msg


#main回车
if __name__ == '__main__':
    #打开浏览器 get_driver  类方法=类名.类方法()
    driver = DriverUtil.get_driver()
    #打开页面，暂停两秒
    driver.get("http:www.baidu.com")
    driver.find_element_by_link_text('设置').click()
    time.sleep(2)
    filename = './nud%s.png'% time.strftime('%Y%m%d%H%M%S')
    driver.get_screenshot_as_file(filename)
    #关闭浏览器
    DriverUtil.quit_driver()
