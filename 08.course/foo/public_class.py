import sys
import os
import pickle

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)
path_path = os.path.join(path, "database")

from log.log_print import log_print
from conf.settings import database_name

login_tag = False


def is_login(func):
    """
    判断学生账号是否登陆装饰器
    :param func: 传入的函数名
    """
    def inner(self, *args):
        global login_tag
        if not login_tag:
            account = input("please input student account:")
            password = input("please input student password:")
            if Public.student_login(self, account, password):
                login_tag = True
        if login_tag:
            func(self, *args)
    return inner


class Public(object):
    """
    公共类，里面包含一些公用函数方法
    """
    def __init__(self):
        pass

    def dumps(self, db_path, information_dict):
        """
        存入数据
        :param db_path:
        :param information_dict:
        :return:
        """
        with open(db_path, "wb")as f:
            f.write(pickle.dumps(information_dict))
            f.flush()

    def loads_data(self, file_name):
        """
        取出数据
        :param db_path:
        :return:
        """
        if os.path.exists(os.path.join(path_path, database_name[file_name])):
            with open(os.path.join(path_path, database_name[file_name]), "rb")as f:
                data = pickle.loads(f.read())
                return data
        else:
            log_print("数据表%s不存在" % database_name[file_name])
            return False

    def produce_id(self, file_name):
        """
        产生学生编号
        :param file_name:
        :return:
        """
        id_list = []
        data_dict = Public.loads_data(self, file_name)
        print(data_dict)
        if Public.loads_data(self, file_name):
            for key in data_dict[file_name]:
                id_list.append(int(key))
            new_id = id_list[-1] + 1
        else:
            new_id = 1001
        return new_id

    def student_login(self, account, password):
        """
        判断学生账号密码是否正确
        :param account:
        :param password:
        :return:
        """
        data_account = []
        student_dict = Public.loads_data(self, "student")
        for key in student_dict["student"]:
            data_account.append(key)
        if account in data_account:
            if password == student_dict["student"][account]["password"]:
                log_print("学生编号%s，登陆成功" % account)
                return True
            else:
                log_print("学生编号%s，密码错误" % account)
        else:
            log_print("学生编号%s不存在" % account)

    def check_teacher(self, teacher_name):
        """
        判断讲师是否存在
        :param teacher_name:讲师名字
        :return:
        """
        teacher_dict = Public.loads_data(self, "teacher")
        teachers = []
        for key in teacher_dict:
            teachers.append(key)
        if teacher_name in teacher_name:
            return True
        else:
            log_print("讲师%s不存在" % teacher_name)


if __name__ == "__main__":
    P = Public()
    print(P.loads_data("course"))
    print(P.loads_data("student"))
    # print(P.loads_data("classroom"))
    # print(P.loads_data("teacher"))
    # print(P.loads_data("school"))