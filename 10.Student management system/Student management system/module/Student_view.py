import os
import sys
path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from db import create_table
from conf.settings import student_menu, date_time, time_time
from log.log_print import log_print


class StudentView(object):
    def __init__(self):
        self.session = create_table.session

    def student_view_main(self):
        while True:
            print(student_menu.format(time_time, date_time))
            choice = input("\033[32;0m input your choice:\033[0m")
            menu = {
                "1": self.check_homework_score,
                "2": self.commit_homework,
                "3": self.check_the_ranking,
                "4": exit
            }
            if choice in menu:
                menu[choice]()
            else:
                log_print("\033[31;0m Selection is invalid\033[0m")

    def check_homework_score(self):
        """
        输入学生姓名和班级，查询作业成绩
        :return:
        """
        values = input("\033[32;0m input student name and class_name,separated by space:\33[0m").strip()
        student_name, class_name = values.split()
        #study_record = self.session.query(create_table.StudyRecord).all()
        student_id = self.session.query(create_table.StudentTable).\
            filter(create_table.StudentTable.student_name == student_name).first().id
        class_id = self.session.query(create_table.ClassTable).\
            filter(create_table.ClassTable.class_name == class_name).first().id
        course_m2m_class_id = self.session.query(create_table.CourseM2MClass).\
            filter(create_table.CourseM2MClass.class_id == class_id).first().id
        student_score = self.session.query(create_table.StudyRecord).\
            filter(create_table.StudyRecord.student_id == student_id and create_table.StudyRecord.course_m2m_class_id ==
                   course_m2m_class_id).first().score
        print("student_score:", student_score)
        log_print("check the students score successful")

    def commit_homework(self):
        """
        输入学生姓名和班级,提交作业
        :return:
        """
        values = input("\033[32;0m input student name and class_name,separated by space:\033[0m").strip()
        student_name, class_name = values.split()
        # study_record = self.session.query(create_table.StudyRecord).all()
        # print(study_record)
        student_id = self.session.query(create_table.StudentTable).\
            filter(create_table.StudentTable.student_name == student_name).first().id
        class_id = self.session.query(create_table.ClassTable).\
            filter(create_table.ClassTable.class_name == class_name).first().id
        course_m2m_class_id = self.session.query(create_table.CourseM2MClass).\
            filter(create_table.CourseM2MClass.class_id == class_id).first().id
        self.session.query(create_table.StudyRecord).\
            filter(create_table.StudyRecord.student_id == student_id and create_table.StudyRecord.course_m2m_class_id ==
                   course_m2m_class_id).update({create_table.StudyRecord.homework_status: "Yes"})
        self.session.commit()
        log_print("commit homework successful")

    def check_the_ranking(self):
        """
        输入班级名称，查询班级名称和成绩
        :return:
        """
        student_dict = dict()
        class_name = input("\033[32;0m input class_name:\033[0m ").strip()
        students = self.session.query(create_table.ClassTable).filter(create_table.ClassTable.class_name == class_name).first()
        class_id = self.session.query(create_table.ClassTable).\
            filter(create_table.ClassTable.class_name == class_name).first().id
        course_m2m_class_id = self.session.query(create_table.CourseM2MClass).\
            filter(create_table.CourseM2MClass.class_id == class_id).first().id
        for student in students.students:
            student_score = self.session.query(create_table.StudyRecord).\
                filter(create_table.StudyRecord.student_id == student.id and
                       create_table.StudyRecord.course_m2m_class_id == course_m2m_class_id).first().score
            student_dict.setdefault(student.student_name, student_score)
        student_rank = zip(student_dict.keys(), student_dict.values())
        score_rank = sorted(student_rank)
        print("class rankings", score_rank)
        log_print("check the score ranking successful")

if __name__ == "__main__":
    m = StudentView()
    m.student_view_main()