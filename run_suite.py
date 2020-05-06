# TestSuite（测试套件）
# 代码步骤
# 1. 导包
import time
import unittest

from case.test_login import TestLogin
from report.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
# 3. 组装测试用例
# loader = unittest.TestLoader
suite.addTest(unittest.makeSuite(TestLogin))
# suite = loader.discover(start_dir='./case',pattern='test*.py')
# suite.addTest(unittest.makeSuite(Test_Lunbotu))
# suite.addTest(unittest.makeSuite(Test_click))


#加上时间戳
report = './report/report %s.html' % time.strftime('%H%m%d%H%M%S')
with open(report,'wb')as f:

    runner = HTMLTestRunner(stream=f,title='登录')
    runner.run(suite)

# runner = unittest.TextTestRunner()
