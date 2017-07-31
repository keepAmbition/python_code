import sys
import os

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from conf.templates import default_menu
from conf.settings import date_time, time_time
from log.log_print import log_print
from foo.student_class import SubStudent
from foo.admin_class import SubAdmin
from foo.teacher_class import SubTeacher


class Main(object):
    def main(self):
        while True:
            print(default_menu.format(time_time, date_time))
            choice = input("输入你的选择")
            menu = {
                "1": SubStudent.student_main,
                "2": SubTeacher.teacher_main,
                "3": SubAdmin.admin_main,
                "4": exit
            }
            if choice in menu:
                menu[choice](self)
            else:
                log_print("选择无效")


if __name__ == "__main__":
    m = Main()
    m.main()