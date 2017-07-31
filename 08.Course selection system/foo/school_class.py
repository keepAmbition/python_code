import sys
import os

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)
db_path = os.path.join(path, "database")


from foo.public_class import Public
from foo.teacher_class import Teacher
from foo.student_class import Student
from conf.settings import database_name
from log.log_print import log_print


class Course(object):
    def __init__(self, course_name, course_tuition, course_cycle):
        self.course_name = course_name
        self.course_tuition = course_tuition
        self.course_cycle = course_cycle


class Classroom(object):
    def __init__(self, classroom_name, classroom_course, classroom_teacher):
        self.classroom_name = classroom_name
        self.classroom_course = classroom_course
        self.classroom_teacher = classroom_teacher


class School(Public):
    def __init__(self):
        Public.__init__(self)

    def create_school(self):
        """
        创建学校
        :return:
        """
        school_name = input("school name:")
        school_place = input("school place:")
        palace_dict = {"school place": school_place}
        if not Public.loads_data(self, "school"):
            school_dict = {"school": {school_name: {palace_dict}}}
            Public.dumps(self, os.path.join(db_path, database_name["school"]), school_dict)
        else:
            data_school_dict = Public.loads_data(self, "school")
            print(data_school_dict)
            data_school_dict["school"].setdefault(school_name, palace_dict)
            Public.dumps(self, os.path.join(db_path, database_name["school"]), data_school_dict)
        log_print("创建学校%s成功" % school_name)

    def create_course(self):
        """
        创建课程
        :return:
        """
        course_name = input("course name:")
        course_tuition = input("course tuition:")
        course_cycle = input("course cycle:")
        c = Course(course_name, course_tuition, course_cycle)
        course_dict = {course_name: {}}
        course_dict[course_name]["course tuition"] = c.course_tuition
        course_dict[course_name]["course cycle"] = c.course_cycle
        if not Public.loads_data(self, "course"):
            Public.dumps(self, os.path.join(db_path, database_name["course"]), course_dict)
            log_print("创建%s表成功" % database_name["course"])
            log_print("创建课程%s成功" % course_name)
        else:
            data_course_dict = Public.loads_data(self, "course")
            data_course_dict.setdefault(course_name, course_dict[course_name])
            Public.dumps(self, os.path.join(db_path, database_name["course"]), data_course_dict)
            log_print("创建课程%s成功" % course_name)

    def create_classroom(self):
        """
        创建班级
        :return:
        """
        classroom_name = input("classroom_name:")
        classroom_course = input("classroom_course:")
        classroom_teacher = input("classroom_teacher:")
        classroom_dict = {classroom_name: {}}
        c = Classroom(classroom_name, classroom_course, classroom_teacher)
        classroom_dict[classroom_name]["classroom course"] = c.classroom_course
        classroom_dict[classroom_name]["classroom teacher"] = c.classroom_teacher
        if not Public.loads_data(self, "classroom"):
            Public.dumps(self, os.path.join(db_path, database_name["classroom"]), classroom_dict)
            log_print("创建%s表成功" % database_name["classroom"])
            log_print("创建班级-%s成功" % classroom_name)
        else:
            data_classroom_dict = Public.loads_data(self, "classroom")
            data_classroom_dict.setdefault(classroom_name, classroom_dict[classroom_name])
            Public.dumps(self, os.path.join(db_path, database_name["classroom"]), data_classroom_dict)
            log_print("创建班级-%s成功" % classroom_name)


    def create_teacher(self):
        """
        创建讲师
        :return:
        """

        teacher_name = input("teacher_name:")
        teacher_salary = input("teacher_salary:")
        teacher_school = input("teacher_school:")
        teacher_dict = {teacher_name: {}}
        t1 = Teacher(teacher_name, teacher_salary, teacher_school)
        teacher_dict[teacher_name]["teacher salary"] = t1.teacher_salary
        teacher_dict[teacher_name]["teacher school"] = t1.teacher_school
        if not Public.loads_data(self, "teacher"):
            Public.dumps(self, os.path.join(db_path, database_name["teacher"]), teacher_dict)
            log_print("创建%s表成功" % database_name["teacher"])
            log_print("创建讲师%s成功" % teacher_name)
        else:
            data_teacher_dict = Public.loads_data(self, "teacher")
            data_teacher_dict.setdefault(teacher_name, teacher_dict[teacher_name])
            Public.dumps(self, os.path.join(db_path, database_name["teacher"]), data_teacher_dict)
            log_print("创建讲师%s成功" % teacher_name)







if __name__ == "__main__":
    s = School()
    s.create_school()
    s.create_teacher()
    s.create_student()
    s.create_classroom()
    s.create_course()