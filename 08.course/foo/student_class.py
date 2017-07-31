import sys
import os

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)
db_path = os.path.join(path, "database")

from foo.public_class import Public, is_login
from conf.templates import student_menu
from conf.settings import date_time, time_time
from conf.settings import database_name
from log.log_print import log_print


class Student(object):
    def __init__(self, student_name, student_class, student_school):
        self.student_name = student_name
        self.student_class = student_class
        self.student_school = student_school

    def register(self):
        """
        学生注册
        :return:null
        """
        student_dict = {}
        student_name = input("student_name:")
        student_school = input("student_school:")
        student_class = input("student_class:")
        stu = Student(student_name, student_class, student_school)
        student_dict["student_name"] = stu.student_name
        student_dict["student_class"] = stu.student_class
        student_dict["student_school"] = stu.student_school
        student_dict["password"] = input("password")
        # 0代表未交学费 1代表已交学费
        student_dict["is_pay_tuition"] = 0
        new_id = Public.produce_id(self, "student")
        if not Public.loads_data(self, "student"):
            data_student_dict = {"student": {str(new_id): student_dict}}
        else:
            data_student_dict = Public.loads_data(self, "student")
            data_student_dict["student"].setdefault(str(new_id), student_dict)
        Public.dumps(self, os.path.join(db_path, database_name["student"]), data_student_dict)
        log_print("学生%s注册成功" % student_name)

    @is_login
    def pay_money(self):
        """
        缴纳学费
        :return:
        """
        choice_course = input("please choice course:")
        student_id = input("请输入你的学生编号：")
        student_dict = Public.loads_data(self, "student")
        tuition = Public.loads_data(self, "course")[choice_course]["course tuition"]
        log_print("课程%s需缴纳学费%s元！" % (choice_course, tuition))
        # 没有特意去做一个支付接口，所以很形式的意思一下
        money = input("请缴纳学费：")
        if money.isdigit() and money == tuition:
            student_dict["student"][student_id]["is_pay_tuition"] = 1
            Public.dumps(self, os.path.join(db_path, database_name["student"]), student_dict)
            log_print("课程%s缴纳学费成功！" % choice_course)
        else:
            log_print("课程%s缴纳学费失败请重新再试！" % choice_course)

    @is_login
    def choice_class(self):
        """
        选择班级
        :return:
        """
        account = input("请输入你的学生编号：")
        choice_class = input("请输入选择的班级：")
        student_dict = Public.loads_data(self, "student")
        old_class = student_dict["student"][account]["student_class"]
        student_dict["student"][account]["student_class"] = choice_class
        Public.dumps(self, os.path.join(db_path, database_name["student"]), student_dict)
        log_print("学生%s从班级%s调整至班级%s!" % (account, old_class, choice_class))


#学员视图类，继承Student类
class SubStudent(Student):
    def __init__(self):
        pass

    def student_main(self):
        menu_dic = {
            '1': Student.register,
            '2': Student.pay_money,
            '3': Student.choice_class,
            '4': exit
        }

        while True:
            print(student_menu.format(time_time, date_time))
            choice = input("请选择：").strip()
            if choice in menu_dic:
                menu_dic[choice](self)
            else:
                log_print("选择无效，请重新选择")




if __name__ == "__main__":
    s = SubStudent()
    s.student_main()