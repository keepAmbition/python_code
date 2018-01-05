import sys
import os

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from conf.settings import default_menu, date_time, time_time
from db.create_test_data import CreateData
from log.log_print import log_print
from module.Student_view import StudentView
from module.Teacher_view import TeacherView


class Main(CreateData, StudentView, TeacherView):
    def main(self):
        while True:
            print(default_menu.format(time_time, date_time))
            choice = input("\033[32;0m input your choice:\033[0m")
            menu = {
                "1": CreateData.create_data,
                "2": TeacherView.teacher_view_main,
                "3": StudentView.student_view_main,
                "4": exit
            }
            if choice in menu:
                menu[choice](self)
            else:
                log_print("\033[31;0m Selection is invalid\033[0m")


if __name__ == "__main__":
    m = Main()
    m.main()