import unittest
import  requests
from api.UserAPI import UserLogin
import json
# 参数化导包
from parameterized import parameterized
# 参数化步骤2 设置文件解析
import app
import json
import unittest

import requests
# 参数化导包
from parameterized import parameterized

# 参数化步骤2 设置文件解析

from api.UserAPI import UserLogin


def read_json():
    #return [("13712273958","123456","8888",1,"登录成功"),("13712273956","123456","8888",-1,"账号有误"),("13712273958","12345","8888",-2,"密码错误")]
# 怎么读取json
# 1.设置一个接收数据的列表
    data = []
#     2.开启文件流,读数据并将数据导入列表
    with open(app.PRO_PATH+ "/data/haha.json", "r", encoding="utf-8")as f:
        for value in json.load(f).values():
            data.append((value.get("username"),
                         value.get("password"),
                         value.get("verify_code"),
                         value.get("status"),
                         value.get("msg")))
    return data
# 创建测试类
class TestUser(unittest.TestCase):
    def setUp(self):
        self.session =requests.Session()
        # 创建UserLogin对象
        self.userlogin =UserLogin()

    def tearDown(self):
     self.session.close()
#     测试函数1:获取验证码
    def test_get_verify_code(self):

        # 1.请求业务
        # 调用get_verify_code函数
        response = self.userlogin.get_verify_code(self.session)

         # 2.断言
        self.assertEqual(200,response.status_code)
        self.assertIn("image",response.headers.get("Content-Type"))
    # 创建函数2

    def test_Login(self):
        # 1.请求业务
        respones=  self.userlogin.get_verify_code(self.session)
        respones2 = self.userlogin.login(self.session,"13712273958","123456","8888")
        # 2.断言
        print(respones2.json())

    @parameterized.expand(read_json())
    def test_Login_red(self,username,password,verify_code,status,msg):
        print("-"*100 )
        print( username, password, verify_code, status, msg)
        response1 = self.userlogin.get_verify_code(self.session)

        response2 = self.userlogin.login(self.session,username, password, verify_code)
        self.assertEqual(status,response2.json().get("status"))
        self.assertIn(msg,response2.json().get("msg"))