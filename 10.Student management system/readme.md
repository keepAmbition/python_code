```
students management(sqlalchemy)/
|-- bin/
|   |-- start.py                     #程序启动主入口
|   
|--db/
|   |-- create_table.py              #创建表结构
|   |-- create_test_table.py         #一键创建测试数据
|
|-- conf/
|   |-- settings.py                  #配置
|               
|-- module/
|   |-- main.py                      #程序主逻辑入口
|   |-- Student_view.py              #学员视图
|   |-- Teacher_view.py              #讲师视图
|
|-- log/
|   |-- log.txt                      #日志
|   |-- log_print.py                 #日志打印函数
|
基于sqlalchemy 的学员管理系统，可执行如下功能：
一、学生视图：1、提交作业、2、查看作业成绩、3、查看班级成绩排名
二、讲师视图：1、创建班级、2、根据QQ号分班、3、创建上课记录、4、批改成绩

一键创建的初始测试数据为：
students : student_name="stu1", QQ="111111" | student_name="stu2", QQ="000000"
teacher : teacher_name="tea1" | teacher_name="tea2"
class : class_name="class-1", class_course="Python" | class_name="class-2", class_course="JAVA"

注意事项：
1、在进入视图之前，需要一键创建原始测试数据
2、需要先进入讲师视图创建上课记录后，才能进入学生视图操作（没有上课记录，相关表无法关联）
3、study_record表中 status 代表考勤记录（默认“YES”），homework_status代表是否提交作业（默认“NO”）
```
