import sys
import os

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)
db_path = os.path.join(path, "database")

from foo.school_class import School
from conf.templates import admin_menu
from conf.settings import date_time, time_time
from log.log_print import log_print


class Admin(School):
    def __init__(self):
        School.__init__(self)

    def add_teacher(self):
        """
        此函数调用School类的创建讲师方法，创建讲师
        :return:null
        """
        School.create_teacher(self)

    def add_classroom(self):
        """
        此函数调用School类的创建班级方法，创建班级
        :return:null
        """
        School.create_classroom(self)

    def add_course(self):
        """
        此函数调用School类的创建课程方法，创建课程
        :return:null
        """
        School.create_course(self)

    def add_school(self):
        """
        此函数调用School类的创建学校方法，创建学校
        :return:null
        """
        School.create_school(self)


class SubAdmin(Admin):
    def __init__(self):
        pass

    def admin_main(self):
        menu_dic = {
            '1': Admin.add_teacher,
            '2': Admin.add_course,
            '3': Admin.add_classroom,
            '4': Admin.add_school,
            "5": exit
        }

        while True:
            print(admin_menu.format(time_time, date_time))
            choice = input("请选择：").strip()
            if choice in menu_dic:
                menu_dic[choice](self)
            else:
                log_print("选择无效，请重新选择")

if __name__ == "__main__":
    a = SubAdmin()
    a.admin_main()