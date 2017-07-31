import datetime
import os
# 数据表单名
database_name = {"school": "school_data", "teacher": "teacher_data", "student": "student_data", "course": "course_data",
                 "classroom": "classroom_data"}


# 日期
date_time = datetime.datetime.now().date()
# 当前时间
time_time = datetime.datetime.now().strftime("%H:%M:%S")
