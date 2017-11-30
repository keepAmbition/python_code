**readme**

Fabric/
|-- bin/
|   |-- __init__.py
|   |-- Fabric_run.py                    #启动程序入口 
|
|-- conf/
|   |-- host_dict.py                    #保存着远程主机的host、username、password                   
|   
|-- db/ 
|-- get_save_file                #从远程主机get下来的文件保存处
|-- put_file                     #测试文件保存处，用于put文件至远程主机       
|   |-- test                     
|   |-- test1
|   |-- test2
|   |-- test3
|   
|-- foo/            
|   |-- main_class.py                    #主类，程序功能实现类   
|
|-- log/
|   |-- log                  #操作日志
|   |-- log_print.py         #打印日志模块
|   

				        
程序包含模仿简单实现了主机管理功能,包含以下小功能：
    1、    get   文件名 下载文件
    2、    push  文件名 上传文件
    3、    cd    路径   切换目录
    4、    ls    展示当前目录下文件
        
调试时，注意点如下：
1、远程主机处于开启状态；
2、将host_dict.py文件中HOST_MAP中的host,port,username,password更换成处于开启状态的远程主机信息;
3、put 文件时，请从put_file目录中选取文件进行测试（test，test1，test2，test3），其实可以写成根据任意路径上的文件进行put,但是为了规范点，就专门弄了一个测试目录