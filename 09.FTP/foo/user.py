import os
import sys

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)




from conf.settings import log_path, db_path
from foo.public import Public
from log.log_print import log_print


class User(Public):
    def __init__(self, name, password):
        super(User, self).__init__()
        self.name = name
        self.password = password

    def add_user(self):
        """
        添加新用户
        :return:
        """
        user_dict = {}
        name = input("name:")
        password = input("password")
        u = User(name, password)
        user_dict["password"] = u.password
        user_dict["is_locked"] = 0
        if not os.path.exists(os.path.join(db_path, name)):
            os.mkdir(os.path.join(db_path, name))
            user_path = os.path.join(db_path, name)
            user_dict = {name: user_dict}
            Public.write_data(self, os.path.join(user_path, "user"), user_dict)
            log_print("新增%s用户信息成功" % name)
        else:
            log_print("用户已存在")

    @staticmethod
    def login(self):
        name = input("name:")
        user_path = os.path.join(os.path.join(db_path, name), "user")
        if Public.check_account(self, user_path, name):
            if Public.check_password(self, user_path, name):
                return True

login_tag = False


def login_magic(func):
    """
    装饰器:验证是否登陆
    :param func: 传入函数名
    :return:
    """
    def login_inner(*args):
        global login_tag
        if not login_tag:
            User.login()
            login_tag = True
        if login_tag:
            func(*args)
    return login_inner

if __name__ == "__main__":
    u = User("aa","aa")
    u.add_user()
    # User.login(u)
