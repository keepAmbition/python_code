import os
import sys

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from log.log_print import log_print
from db import create_table


class CreateData(object):
    def __init__(self):
        self.session = create_table.session  # 创建与数据库的会话session

    def create_data(self):
        """
        创建表结构和原始测试数据
        :return:
        """
        #创建表结构
        create_table.Base.metadata.create_all(create_table.connect)
        """创建原始测试数据"""
        #讲师数据
        tea1 = create_table.TeacherTable(teacher_name="tea1")
        tea2 = create_table.TeacherTable(teacher_name="tea2")
        #学生数据
        stu1 = create_table.StudentTable(student_name="stu1", QQ="111111")
        stu2 = create_table.StudentTable(student_name="stu2", QQ="000000")
        #班级数据
        class1 = create_table.ClassTable(class_name="class-1", class_course="Python")
        class2 = create_table.ClassTable(class_name="class-2", class_course="JAVA")
        # #课程数据
        # course1 = create_table.CourseTable(course_name="python-day1")
        # course2 = create_table.CourseTable(course_name="java-day1")
        # #学习记录数据
        # record1 = create_table.StudyRecord(course_m2m_class_id=1, student_id=1, score=80)
        # record2 = create_table.StudyRecord(course_m2m_class_id=2, student_id=1, score=90)
        # record3 = create_table.StudyRecord(course_m2m_class_id=1, student_id=2, score=88)
        # record4 = create_table.StudyRecord(course_m2m_class_id=2, student_id=2, score=99)
        # #课程—班级关联数据
        # course_m2m_class1 = create_table.CourseM2MClass(class_id=1, course_id=1)
        # course_m2m_class2 = create_table.CourseM2MClass(class_id=2, course_id=2)
        #讲师—班级关联数据
        tea1.classes = [class1, class2]
        #学生—班级关联数据
        class1.students = [stu1, stu2]
        self.session.add_all([tea1, tea2, stu1, stu2, class1, class2])
        self.session.commit()
        log_print("create test data successful")

if __name__ == "__main__":
    c = CreateData()
    c.create_data()
