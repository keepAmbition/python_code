**readme**
```
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
				        
程序包含模仿简单实现了select版 FTP 功能,包含以下小功能：
    1、    get   file name 下载文件 (file name 指的是bin目录下的， server_run.py 和 client_run.py 两个文件，如果要上传，下载其他路径下的文件需要加上路径)
    2、    put   file name 上传文件
```
