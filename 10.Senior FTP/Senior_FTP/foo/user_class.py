import os
import sys
import hashlib

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)
user_data_file = os.path.join(os.path.join(path, "db"), "user_data")
print(user_data_file)

from foo.public_class import Public
from log.log_print import log_print


class User(Public):
    def __init__(self, name, password, phone):
        self.name = name
        self.password = password
        self.phone = phone
        Public.__init__(self)

    def register(self):
        """
        注册
        :return:
        """
        m = hashlib.md5()
        user_dict = {}
        numbers = []
        name = input("请输入你要注册的名字：")
        password = input("请输入密码：")
        phone = input("请输入用户电话：")
        u = User(name, password, phone)
        user_dict["name"] = u.name
        m.update(u.password.encode("utf-8"))
        user_dict["password"] = m.hexdigest()
        user_dict["phone"] = u.phone
        user_dict["memory"] = 50
        # print(user_dict)
        if not Public.read_data_r(self, user_data_file):
            data = {"user": {phone: user_dict}}
            Public.write_data_w(self, user_data_file, data)

        else:
            old_user_data = Public.read_data_r(self, user_data_file)
            for i in old_user_data["user"]:
                numbers.append(i)

            if phone in numbers:
                log_print("该手机号已被注册，请使用新手机号注册")
            else:
                old_user_data["user"].setdefault(phone, user_dict)
                Public.write_data_w(self, user_data_file, old_user_data)
        os.mkdir(os.path.join(os.path.join(os.path.join(path, "db"), "user"), name))
        log_print("用户%s，注册成功" % name)

    def login(self):
        """
        登陆
        """
        while True:
            account = input("请输入名称：")
            if self.check_account(account):
                    if self.check_password(account):
                        log_print("登录成功")
                        return account
            else:
                continue

    def check_account(self, account):
        """
        检查账号合法性
        :param account:账号
        :return:
        """
        accounts = []
        locked_account = []
        user_dict = Public.read_data_r(self, user_data_file)
        for i in user_dict["user"]:
            if user_dict["user"][i].get("locked") == "1":
                locked_account.append(user_dict["user"][i].get("name"))
            accounts.append(user_dict["user"][i]["name"])

        if account in accounts:
            if account not in locked_account:
                return True
            else:
                log_print("账号已被锁定，请重新输入")
        else:
            log_print("账号不存在，请重新输入")

    def check_password(self, account):
        """
        传入参数（账号），检查密码输入是否非法
        """
        count = 0
        user_dict = Public.read_data_r(self, user_data_file)
        while count < 3:
            m1 = hashlib.md5()
            password = input("请输入密码：")
            m1.update(password.encode("utf-8"))
            for i in user_dict["user"]:
                if user_dict["user"][i]["name"] == account and user_dict["user"][i]["password"] == m1.hexdigest():
                    return True
            else:
                count += 1
                log_print("密码错误，你还有%d次输入机会" % (3 - count))
                continue
        else:
            log_print("密码错误次数过多，账号%s已被锁定" % account)
            for j in user_dict["user"]:
                if user_dict["user"][j]["name"] == account:
                    user_dict["user"][j].setdefault("locked", "1")
                    Public.write_data_w(self, user_data_file, user_dict)

# login_tag = False
#
#
# def login_magic(func):
#     """
#     装饰器:验证是否登陆
#     :param func: 传入函数名
#     :return:
#     """
#     def login_inner(self, *args):
#         global login_tag
#         if not login_tag:
#             U = User("AA", "AA", "AA")
#             U.login()
#             login_tag = True
#         if login_tag:
#             func(self, *args)
#     return login_inner



if __name__ == "__main__":
    u = User("sadasd","asdasd","adasd")
    u.register()