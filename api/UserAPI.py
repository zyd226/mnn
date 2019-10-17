import app


class UserLogin:
    # 函数验证码请求
    def get_verify_code(self,session):
        # session.get("验证码URL")

        return session.get(app.BASE_URI + "index.php?m=Home&c=User&a=verify")
    # 登录业务请求
    def login(self,session,username,password,verify_code):
        myData =   {"username": username,
                   "password": password,
                   "verify_code": verify_code}

        return session.post(app.BASE_URI + "index.php?m=Home&c=User&a=do_login", data=myData)