**readme**
<<<<<<< HEAD
···
=======
'''
>>>>>>> 620b9c504a658494b7e67b41c8e6745a03b60983
Senior_FTP/
|-- bin/
|   |-- __init__.py
|   |-- FTP_server_run.py                #启动服务端程序入口
|   |-- FTP_client_run.py                #启动客户端程序入口
|
|-- conf/
|   |-- templates.py                     #程序UI界面                   
|   
|-- db/ 
|   |-- server_save_file                 #客户端push到服务端的文件保存目录
|   |-- user                             #用户目录包含所有用户信息         
|   |-- user_data                        #用户信息表（账号，密码，磁盘配额等信息）
|
|-- foo/
|   |-- client_class.py                  # 客户端类
|   |-- server_class.py                  #服务端类
|   |-- public_class.py                  #公共类，存放公共方法
|   |-- user_calss.py                    #用户类
|   |-- main_class.py                    #主类 集成各个类方法   
|   |-- test                             #测试文本，测试get,push cmd命令的文本
|
|-- log/
|   |-- log                  #操作日志
|   |-- log_print.py         #打印日志模块
|   
<<<<<<< HEAD
···
=======
'''
>>>>>>> 620b9c504a658494b7e67b41c8e6745a03b60983
程序的用户账户：        账号：QQ   密码：123
                        账号：QQ1  密码：123
				        账号：QQ2  密码：123
				        
						
程序包含模仿简单FTP,然后包含以下小功能：
用户注册、用户登录（支持多用户登陆执行client操作）、
client: get   文件名 下载文件
        push  文件名 上传文件
        cd    路径   切换目录
        ls    展示当前目录下文件
        
其中 get、push 包含断点续传,进度条功能，get文件时还有磁盘配额校验（新用户注册时，默认50M空间）
cd 切换路径时，对公共目录路径切换无限制，在user目录下，只能切换至登陆用户路径，其他用户目录路径无法访问