**test**
···
**1. case1 用户注册、登陆**
====================

                             FTP功能选择

时间:17:24:43                                           今天:2017-10-31
-------------------------------------------------------------------------
【1】用户注册                               【2】用户登录
【3】上传/下载/查看当前目录下文件/修改目录   【4】帮助
【5】退出


请选择：1
请输入你要注册的名字：QQ5
请输入密码：123
请输入用户电话：115
2017-10-31 17:24:49,790 - test.log - INFO - 用户QQ5，注册成功

-------------------------------------------------------------------------
                             FTP功能选择

时间:17:24:43                                           今天:2017-10-31
-------------------------------------------------------------------------
【1】用户注册                               【2】用户登录
【3】上传/下载/查看当前目录下文件/修改目录   【4】帮助
【5】退出


请选择：2
请输入名称：QQ5
请输入密码：123
2017-10-31 17:24:58,293 - test.log - INFO - 登录成功



 

**2. case Client端get、push、cd、ls**
=================================


-------------------------------------------------------------------------
                             FTP功能选择

时间:17:24:43                                           今天:2017-10-31
-------------------------------------------------------------------------
【1】用户注册                               【2】用户登录
【3】上传/下载/查看当前目录下文件/修改目录   【4】帮助
【5】退出


请选择：3
请输入名称：QQ
请输入密码：123
2017-10-31 17:28:16,670 - test.log - INFO - 登录成功
**cmd:>>>>ls**
ls
当前目录下文件：
FTP_client_run.py
FTP_server_run.py
**cmd:>>>>cd C:/Users/dell/PycharmProjects/untitled/home_work/Senior_FTP/foo**
cd C:/Users/dell/PycharmProjects/untitled/home_work/Senior_FTP/foo
C:/Users/dell/PycharmProjects/untitled/home_work/Senior_FTP/foo
目录已切换至: C:\Users\dell\PycharmProjects\untitled\home_work\Senior_FTP\foo
**cmd:>>>>ls**
ls
当前目录下文件：
client_class.py
main_class.py
public_class.py
server_class.py
test
user_class.py
**cmd:>>>>get test**
get test
**本次下载内容大小为:5M,剩余可用内容为：892M**
即将接收数据大小: 6094
[====================================================================================================] 100.00%
md5值一致，校验通过
**cmd:>>>>push test**
push test
即将上传的文件大小为:5M
服务端准备好接收数据内容了
[====================================================================================================] 100.00%
 md5值一致，校验通过
**cmd:>>>>ls**
ls
当前目录下文件：
client_class.py
main_class.py
public_class.py
server_class.py
test
user_class.py
__pycache__


**3.case 断点续传（get、push）**
=======================

**get 的断点续传**
**cmd:>>>>get client_class.py**
get client_class.py
**本次下载内容大小为:7M,剩余可用内容为：885M**
即将接收数据大小: 7378
[========================================================                                             ] 56.03%



-------------------------------------------------------------------------
                             FTP功能选择

时间:19:20:27                                           今天:2017-10-31
-------------------------------------------------------------------------
【1】用户注册                               【2】用户登录
【3】上传/下载/查看当前目录下文件/修改目录   【4】帮助
【5】退出


请选择：3
请输入名称：QQ
请输入密码：123
2017-10-31 19:20:39,886 - test.log - INFO - 登录成功
**cmd:>>>>cd C:/Users/dell/PycharmProjects/untitled/home_work/Senior_FTP/foo**
cd C:/Users/dell/PycharmProjects/untitled/home_work/Senior_FTP/foo
C:/Users/dell/PycharmProjects/untitled/home_work/Senior_FTP/foo
目录已切换至: C:\Users\dell\PycharmProjects\untitled\home_work\Senior_FTP\foo
**cmd:>>>>get test**
get test
C:\Users\dell\PycharmProjects\untitled\home_work\Senior_FTP\db\user
文件断点续传中》》》
[====================================================================================================] 100.00%







**push的断点续传**
**cmd:>>>>push test**
push test
C:\Users\dell\PycharmProjects\untitled\home_work\Senior_FTP\bin\test
2017-11-01 12:25:45,180 - test.log - INFO - 文件test不存在
cmd:>>>>cd C:/Users/dell/PycharmProjects/untitled/home_work/Senior_FTP/foo
cd C:/Users/dell/PycharmProjects/untitled/home_work/Senior_FTP/foo
C:/Users/dell/PycharmProjects/untitled/home_work/Senior_FTP/foo
目录已切换至: C:\Users\dell\PycharmProjects\untitled\home_work\Senior_FTP\foo
**cmd:>>>>ls**
ls
当前目录下文件：
client_class.py
main_class.py
public_class.py
server_class.py
test
user_class.py
__pycache__
**cmd:>>>>push test**
push test
C:\Users\dell\PycharmProjects\untitled\home_work\Senior_FTP\foo\test
即将上传的文件大小为:5M
服务端准备好接收数据内容了
[====================================                                                                ] 36.45%


-------------------------------------------------------------------------
                             FTP功能选择

时间:11:54:46                                           今天:2017-11-01
-------------------------------------------------------------------------
【1】用户注册                               【2】用户登录
【3】上传/下载/查看当前目录下文件/修改目录   【4】帮助
【5】退出


请选择：3
请输入名称：QQ
请输入密码：123
2017-11-01 11:54:57,197 - test.log - INFO - 登录成功
**cmd:>>>>push test**
push test
C:\Users\dell\PycharmProjects\untitled\home_work\Senior_FTP\bin
文件断点续传中》》》
[====================================================================================================] 100.00%

**cmd:>>>>push client_class.py**
push client_class.py
C:\Users\dell\PycharmProjects\untitled\home_work\Senior_FTP\foo\client_class.py
即将上传的文件大小为:7M
服务端准备好接收数据内容了
[====================================================================================================] 100.00%
 md5值一致，校验通过
 ···