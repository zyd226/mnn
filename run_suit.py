# 导包
import unittest
import time
#创建测试套件对象


from case.TestTPSopUsser import TestUser
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
# 添加测试类或者测试函数
#suite.addTest(TestUser("test_login_red"))
suite.addTest(unittest.makeSuite(TestUser))
# 先创建文件
file_to = "./report/report1"+time.strftime("%Y%m%d%H%M%S")+".html"
# 打开文件流,工具执行套件,并将结果写出

with open(file_to,"wb")as f:
    runner = HTMLTestRunner(f,title ="我的测试报告",description = "v1.0" )
    runner.run(suite)