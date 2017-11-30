**readme**
<<<<<<< HEAD
···
=======
'''
>>>>>>> 620b9c504a658494b7e67b41c8e6745a03b60983
select ftp/
|-- bin/
|   |-- client_run.py                    #启动客户端程序主入口
|   |-- server_run.py                    #启动服务的程序主入口
|   
|-- db/ 
|-- save_get_file                        #保存各个客户端从服务端的get下来的文件
|-- server_save_file                     #保持各个客户端put服务端的文件    
|   
|-- foo/            
|   |-- client_class.py                    #客户端逻辑实现类
|   |-- server_class.py                    #服务端逻辑实现类
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
				        
程序包含模仿简单实现了select版 FTP 功能,包含以下小功能：
    1、    get   file name 下载文件 (file name 指的是bin目录下的， server_run.py 和 client_run.py 两个文件，如果要上传，下载其他路径下的文件需要加上路径)
    2、    put   file name 上传文件
        
这个作业写的很简单，纯粹只是为了实现功能而进行的敷衍性编程，没有添加任何额外的功能，但是也卡了我蛮久（大概一个月左右，就是put 文件至服务端，一直实现不了这个功能，然后我用来测试进行put的文件本来是一首诗，从客户端以二进制读取发送至服务端，然后服务端进行decode(),这里一直报UnicodeDecodeError错误，也找了很久原因，解决不了，只能当成异常给捕获了），最后用一个取巧的办法实习了put上传，蛋疼的一次作业。以后要早点睡觉了，不然写代码的时候都是懵的，效率很低，还老是出错。