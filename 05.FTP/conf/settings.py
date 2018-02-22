import os
import sys

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

# 日志存放路径
log_path = os.path.join(os.path.join(path, "log"), "log")

# 数据库路径
db_path = os.path.join(path, "db")

# 菜单模板
menu = """
-------------------------------------------------------------------------
                             FTP功能选择

时间:{0}                                           今天:{1}
-------------------------------------------------------------------------
【1】用户注册                          【2】用户登录
【3】上传/下载文件                     【4】查看当前目录下文件
【5】退出
"""