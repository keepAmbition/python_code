```
## test ##

- case:1 创建原始测试数据

-------------------------------------------------------------------------
                             学院系统

时间:16:08:23                                               今天:2018-01-05
-------------------------------------------------------------------------
【1】创建表、生成测试数据       【2】讲师视图      【3】学员视图       【4】退出系统

 input your choice:1

2018-01-05 16:08:30,030 - sqlalchemy_practice.log - INFO - create test data successful












- case:2 讲师视图功能演示，实际结果需要在mysql中查看

-------------------------------------------------------------------------
                             学院系统

时间:16:08:23                                               今天:2018-01-05
-------------------------------------------------------------------------
【1】创建表、生成测试数据       【2】讲师视图      【3】学员视图       【4】退出系统

 input your choice:2

-------------------------------------------------------------------------
                             讲师视图

时间:16:08:23                                           今天:2018-01-05
-------------------------------------------------------------------------
【1】创建班级                       【2】根据QQ号分班
【3】创建上课记录                   【4】批改学生成绩
【5】退出系统

 input your choice:1
 input new class name and course, separated by space: **class-3 linux**
2018-01-05 16:09:17,788 - sqlalchemy_practice.log - INFO - create new class successful

-------------------------------------------------------------------------
                             讲师视图

时间:16:08:23                                           今天:2018-01-05
-------------------------------------------------------------------------
【1】创建班级                       【2】根据QQ号分班
【3】创建上课记录                   【4】批改学生成绩
【5】退出系统

 input your choice:2
all student: [student id: 1  student name: stu1  QQ: 111111, student id: 2  student name: stu2  QQ: 000000]
all class: [class name: class-1   class_course: Python, class name: class-2   class_course: JAVA, class name: class-3   class_course: linux]
 input student QQ and class name, separated by space: **111111 class-3**
2018-01-05 16:10:01,876 - sqlalchemy_practice.log - INFO - split class successful

-------------------------------------------------------------------------
                             讲师视图

时间:16:08:23                                           今天:2018-01-05
-------------------------------------------------------------------------
【1】创建班级                       【2】根据QQ号分班
【3】创建上课记录                   【4】批改学生成绩
【5】退出系统

 input your choice:3
all class [class name: class-1   class_course: Python, class name: class-2   class_course: JAVA, class name: class-3   class_course: linux]
 input class name and course name, separated by space: **class-1 python-day1**
2018-01-05 16:10:54,411 - sqlalchemy_practice.log - INFO - create lesson record successful

-------------------------------------------------------------------------
                             讲师视图

时间:16:08:23                                           今天:2018-01-05
-------------------------------------------------------------------------
【1】创建班级                       【2】根据QQ号分班
【3】创建上课记录                   【4】批改学生成绩
【5】退出系统

 input your choice:4
all study record: [ course_m2m_class_id: 1  student_id :1  status:YES  score: 0,  course_m2m_class_id: 1  student_id :2  status:YES  score: 0]
 input student name , class name and score, separated by space: **stu1 class-1 98**
2018-01-05 16:11:32,756 - sqlalchemy_practice.log - INFO - Score the students successful

-------------------------------------------------------------------------
                             讲师视图

时间:16:08:23                                           今天:2018-01-05
-------------------------------------------------------------------------
【1】创建班级                       【2】根据QQ号分班
【3】创建上课记录                   【4】批改学生成绩
【5】退出系统

 input your choice:5
 
 
 
 
 
 
 
 
 

- case:3 学生视图，实际结果需要在mysql中查看
 
-------------------------------------------------------------------------
                             学员视图

时间:16:22:36                                           今天:2018-01-05
-------------------------------------------------------------------------
【1】查看作业成绩       【2】提交作业      【3】查看班级排名        【4】退出系统

 input your choice:1
 input student name and class_name,separated by space:**stu1 class-1**
student_score: 98
2018-01-05 16:22:51,324 - sqlalchemy_practice.log - INFO - check the students score successful

-------------------------------------------------------------------------
                             学员视图

时间:16:22:36                                           今天:2018-01-05
-------------------------------------------------------------------------
【1】查看作业成绩       【2】提交作业      【3】查看班级排名        【4】退出系统

 input your choice:2
 input student name and class_name,separated by space:**stu1 class-1**
2018-01-05 16:23:12,635 - sqlalchemy_practice.log - INFO - commit homework successful

-------------------------------------------------------------------------
                             学员视图

时间:16:22:36                                           今天:2018-01-05
-------------------------------------------------------------------------
【1】查看作业成绩       【2】提交作业      【3】查看班级排名        【4】退出系统

 input your choice:3
 input class_name: **class-1**
class rankings [('stu1', 98), ('stu2', 0)]
2018-01-05 16:23:32,064 - sqlalchemy_practice.log - INFO - check the score ranking successful

-------------------------------------------------------------------------
                             学员视图

时间:16:22:36                                           今天:2018-01-05
-------------------------------------------------------------------------
【1】查看作业成绩       【2】提交作业      【3】查看班级排名        【4】退出系统

 input your choice:4

 
```
