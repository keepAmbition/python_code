import sys
import os

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)
db_path = os.path.join(path, "database")

from conf.settings import date_time, time_time
from conf.templates import teacher_menu
from foo.public_class import Public
from log.log_print import log_print
from conf.settings import database_name


class Teacher(Public):
    def __init__(self, teacher_name, teacher_salary, teacher_school):
        self.teacher_name = teacher_name
        self.teacher_salary = teacher_salary
        self.teacher_school = teacher_school

    def choice_class(self):
        """
        选择班级
        :return:
        """
        teacher_name = input("请输入讲师你的名字:")
        if Public.check_teacher(self, teacher_name):
            class_dict = Public.loads_data(self, "classroom")
            for key in class_dict:
                print(key)
            choice_class = input("请输入你想选择教授的班级：")
            old_teacher_name = class_dict[choice_class]["classroom teacher"]
            class_dict[choice_class]["classroom teacher"] = teacher_name
            Public.dumps(self, os.path.join(db_path, database_name["classroom"]), class_dict)
            log_print("选择班级成功,%s授课讲师已从%s更换成新讲师%s" % (choice_class, old_teacher_name, teacher_name))
        else:
            exit()

    def check_students(self):
        """
        查看班级学生
        :return:
        """
        school_name = input("请输入你所在学校名称：")
        class_name = input("请输入你想查看学生明细的班级：")
        student_dict = Public.loads_data(self, "student")
        print("——————学生明显如下——————")
        for key in student_dict["student"]:
            if student_dict["student"][key]["student_class"] == class_name and student_dict["student"][key]["student_school"] == school_name:
                print(student_dict["student"][key]["student_name"])


    def change_achievement(self):
        """
        修改学生成绩
        :return:
        """
        student_dict = Public.loads_data(self, "student")
        student_name = input("请输入你想打分的学生：")
        student_achievement = input("请输入该学生成绩：")
        for key in student_dict["student"]:
            if student_dict["student"][key]["student_name"] == student_name:
                student_dict["student"][key].setdefault("achievement", student_achievement)
        log_print("打分成功,给学生%s打分为:%s" % (student_name, student_achievement))
        Public.dumps(self, os.path.join(db_path, database_name["student"]), student_dict)


class SubTeacher(Teacher):
    def __init__(self):
        pass

    def teacher_main(self):
        menu_dic = {
            '1': Teacher.choice_class,
            '2': Teacher.check_students,
            '3': Teacher.change_achievement,
            '4': exit
        }

        while True:
            print(teacher_menu.format(time_time, date_time))
            choice = input("请选择：").strip()
            if choice in menu_dic:
                menu_dic[choice](self)
            else:
                log_print("选择无效，请重新选择")


if __name__ == "__main__":
    ST = SubTeacher()
    ST.teacher_main()
