import os
import sys
path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from db import create_table
from conf.settings import teacher_menu, date_time, time_time
from log.log_print import log_print
from sqlalchemy import text


class TeacherView(object):
    def __init__(self):
        self.session = create_table.session

    def teacher_view_main(self):
        while True:
            print(teacher_menu.format(time_time, date_time))
            choice = input("\033[32;0m input your choice:\033[0m")
            menu = {
                "1": self.create_class,
                "2": self.split_class,
                "3": self.create_lesson_record,
                "4": self.score_the_student,
                "5": exit
            }
            if choice in menu:
                menu[choice]()
            else:
                log_print("\033[31;0m Selection is invalid\033[0m")

    def create_class(self):
        """
        创建新班级
        :return:
        """
        class_name = input("\033[32;0m input new class name and course, separated by space:\033[0m ").strip()
        classes, course = class_name.split()
        new_class = create_table.ClassTable(class_name=classes, class_course=course)
        self.session.add(new_class)
        self.session.commit()
        log_print("create new class successful")

    def split_class(self):
        """
        根据学生QQ号分班
        :return:
        """
        all_student = self.session.query(create_table.StudentTable).filter(create_table.StudentTable.id > 0).all()
        print("all student:", all_student)
        all_classes = self.session.query(create_table.ClassTable).filter(create_table.ClassTable.id > 0).all()
        print("all class:", all_classes)
        values = input("\033[32;0m input student QQ and class name, separated by space:\033[0m ").strip()
        student_qq, class_name = values.split()
        student_id = self.session.query(create_table.StudentTable).\
            filter(create_table.StudentTable.QQ == student_qq).first().id
        class_id = self.session.query(create_table.ClassTable).\
            filter(create_table.ClassTable.class_name == class_name).first().id
        self.session.execute("insert into student_m2m_class(student_id,class_id)values(%s,%s)" % (student_id, class_id))
        self.session.commit()
        log_print("split class successful")

    def create_lesson_record(self):
        """
        创建上课记录，为整班添加上课记录，班级上每个学生考勤默认为yes
        :return:
        """
        all_class = self.session.query(create_table.ClassTable).all()
        print("all class", all_class)
        lesson_record = input("\033[32;0m input class name and course name, separated by space:\033[0m ").strip()
        class_name, course_name = lesson_record.split()
        course = create_table.CourseTable(course_name=course_name)
        self.session.add(course)
        self.session.commit()
        class_id = self.session.query(create_table.ClassTable).\
            filter(create_table.ClassTable.class_name == class_name).first().id
        course_id = self.session.query(create_table.CourseTable).\
            filter(create_table.CourseTable.course_name == course_name).first().id
        course_m2m_class = create_table.CourseM2MClass(course_id=course_id, class_id=class_id)
        self.session.add(course_m2m_class)
        self.session.commit()
        course_m2m_class_id = self.session.query(create_table.CourseM2MClass).filter(
            create_table.CourseM2MClass.course_id == course_id and
            create_table.CourseM2MClass.class_id == class_id).first().id
        classes = self.session.query(create_table.ClassTable).filter(create_table.ClassTable.id == 1).first()
        for student in classes.students:
            study_record = create_table.StudyRecord(course_m2m_class_id=course_m2m_class_id, student_id=student.id)
            self.session.add(study_record)
            self.session.commit()
        log_print("create lesson record successful")

    def score_the_student(self):
        """
        批改成绩，学生每门课程默认成绩为0
        :return:
        """
        study_record = self.session.query(create_table.StudyRecord).all()
        print("all study record:", study_record)
        values = input("\033[32;0m input student name , class name and score, separated by space:\033[0m ").strip()
        student_name, class_name, score = values.split()
        student_id = self.session.query(create_table.StudentTable).\
            filter(create_table.StudentTable.student_name == student_name).first().id
        class_id = self.session.query(create_table.ClassTable).\
            filter(create_table.ClassTable.class_name == class_name).first().id
        course_m2m_class_id = self.session.query(create_table.CourseM2MClass).\
            filter(create_table.CourseM2MClass.class_id == class_id).first().id
        self.session.query(create_table.StudyRecord).filter(create_table.StudyRecord.student_id == student_id and
                                                            create_table.StudyRecord.course_m2m_class_id ==
                                                            course_m2m_class_id).update({"score": score})
        self.session.commit()
        log_print("Score the students successful")


if __name__ == "__main__":
    m = TeacherView()
    m.teacher_view_main()