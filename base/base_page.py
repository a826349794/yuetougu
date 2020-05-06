from utils import DriverUtil


class BasePage():
    def __init__(self):
        # 浏览器对象
        self.driver = DriverUtil.get_driver()

        # 元素对象定位方法(定位策略,定位依据)
    def base_find_element(self,location):
        return self.driver.find_element(location[0],location[1])

class BaseHandle():
    def input_text(self,element,text):
        element.clear()
        element.send_keys(text)