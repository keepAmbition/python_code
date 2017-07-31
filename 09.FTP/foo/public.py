import os
import sys
import json

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)
# 数据库路径
data_path = os.path.join(path, "db")

# 上传下载文件保存路径
socket_data_path = os.path.join(path, "conf")

from log.log_print import log_print



class Public(object):
    def __init__(self):
        pass

    def upload_file(self, file_name):
        """
        以二进制方式读取文件
        :param file_name:
        :return:
        """
        with open(os.path.join(socket_data_path, file_name), "rb")as f:
            data = f.read()
            return data

    def save_file(self, file_name, data):
        """
        以二进制方式写入文件
        :param file_name:
        :param data:
        :return:
        """
        with open(os.path.join(socket_data_path, file_name), "wb") as f:
            f.write(data)


    def write_data(self, file_path, data_dict):
        """
        写入数据
        :param file_path:文件路径
        :param data_dict:要写入的数据
        :return:
        """
        with open(file_path, "w+", encoding='utf-8')as f:
            f.write(json.dumps(data_dict))
            f.flush()

    def load_data(self, file_path):
        """
        加载数据
        :param file_path:文件路径
        :return:
        """
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf8")as f:
                data = json.loads(f.read())
                return data


    def check_account(self, user_path, name):
        """
        检测用户账号是否存在或者合法
        :param name: 用户名
        :return:
        """

        user_dict = Public.load_data(self, user_path)
        names = os.listdir(os.path.join(path, "db"))
        if name in names:
            if user_dict[name].get("is_locked") == None or user_dict[name].get("is_locked") == 0:
                return True
            else:
                log_print("用户%s账号被锁定" % name)
        else:
            log_print("用户%s不存在" % name)

    def check_password(self, user_path, name):
        """
        检测密码是否正确，密码输错三次账号被锁定
        :param name: 用户名
        :param password: 密码
        :return:
        """
        user_dict = Public.load_data(self, user_path)
        count = 0
        while count < 3:
            password = input("password:")
            if password == user_dict[name]["password"]:
                log_print("用户%s登录成功" % name)
                return True
            else:
                count += 1
                if count == 3:
                    log_print("用户%s输入错误次数过多，账号被锁定" % name)
                    if user_dict[name].get("is_locked") == None:
                        user_dict[name].setdefault("is_locked", 1)
                        Public.write_data(self, "user", user_dict)
                    else:
                        user_dict[name]["is_locked"] = 1
                        Public.write_data(self, "user", user_dict)
                else:
                    log_print("密码错误，你还剩下%d次机会" % (3 - count))
                    continue

    def check_choice(self, choice):
        """
        判断选择上传或者下载时，其选择是否非法
        :param choice:
        :return:
        """
        choices = ["上传", "下载", "exit"]
        if choice in choices:
            return True
        else:
            log_print("选择无效，请重新选择")

    def view_directory(self):
        """
        查看当前目录下文件
        :return:
        """
        for root, dirs, files in os.walk(path, topdown=False):
            for i in files:
                print(i)

if __name__ == "__main__":
    p = Public()
    p.view_directory()