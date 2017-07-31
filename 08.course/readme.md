**readme**

ATM作业/
|-- bin/
|   |-- __init__.py
|   |-- CSS_Run.py                #程序启动的主入口
|
|-- conf/
|   |-- templates.py             # 存放功能菜单模板
|   |-- setting.py               # 各种配置信息                    
|
|-- foo/
|   |-- admin_class.py             # 管理类，提供管理视图
|   |-- public_class.py            #公共类，存放各种公用模块
|   |-- main_class.py             # 主类，集成各个类
|   |-- school_class.py           #学校类，创建学校
|   |-- teacher_class.py          #讲师类，提供讲师视图
|   |-- student_class.py          #学生类，提供学生视图
|               
|
|-- datebase/
|   |-- classroom_data      # 班级信息数据表
|   |-- course_data         # 课程信息数据表
|   |-- school_data         # 学校信息表
|   |-- teacher_data        # 讲师信息表
|   |-- student_data        # 学生信息表
|
|-- log/
|   |-- log                  #操作日志
|   |-- log_print.py         #打印日志模块
|   


程序的学生登陆账户：    账号：1001 密码：12345
                        账号：1002 密码：12345
				        账号：1003 密码：12345
				        
程序讲师名字：TTTT     QQQQ						
						
程序包含3种视图，学生视图，管理视图、讲师视图，几个视图下分别包含几个小功能。
学生视图：学员注册， 上交学费，选择班级
讲师视图：选择上课班级，查看班级学生明细，给学员打分
管理视图: 创建学校，创建讲师，创建课程，创建班级
