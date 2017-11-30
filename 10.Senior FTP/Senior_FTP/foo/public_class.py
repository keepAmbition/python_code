import os
import sys
import json
import math
import time
import hashlib
import re

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from log.log_print import log_print


class Public(object):
    def __init__(self):
        self.m = hashlib.md5()


    def read_data_r(self, file_name):
        """
        用户信息表读取
        :param file_name: 文件名
        :return:
        """
        if os.path.exists(file_name):
            with open(file_name, "r+", encoding="utf-8")as f:
                data = json.loads(f.read())
                return data
        else:
            log_print("用户数据表不存在,新建用户数据表")
            return False

    def write_data_w(self, file_name, data):
        """
        用户数据信息表写入
        :param file_name: 文件名
        :param data: 要写入的数据
        :return:
        """
        with open(file_name, "w+", encoding="utf_8") as f:
            f.write(json.dumps(data))
            f.flush()

    def check_memory(self, user_name, file_size):
        """
        检查用户磁盘配额是否足够
        :param user_name: 用户名
        :param file_size: 要下载文件的大小
        :return:
        """
        file_name = os.path.join(os.path.join(path, "db"), "user_data")
        user_dict = self.read_data_r(file_name)
        # print(user_dict)
        for i in user_dict["user"]:
            if user_dict["user"][i]["name"] == user_name:
                memory = user_dict["user"][i]["memory"]
                if memory > file_size:
                    user_dict["user"][i]["memory"] = math.floor(memory - file_size)
                    print("本次下载内容大小为:%sM,剩余可用内容为：%sM" % (file_size, math.floor(memory - file_size)))
                    # print(user_dict)
                    self.write_data_w(file_name, user_dict)
                    return True
                else:
                    print("内存不足,无法下载内容")
                    return False

    def tell_pos(self, user_path):
        """
        检查文件最后一个字节的节点
        :param user_path: 文件的路径
        :return:
        """
        with open(user_path, "rb") as f:
            for line in f:
                # print(line)
                self.m.update(line)
                # print(self.m.hexdigest())
            pos = f.tell()     # 判断已下载文件当前进度节点
            return pos

    def check_breakpoint(self, file_name, user_path):
        """
        断电续传功能的实现
        :param file_name:原本文件路径
        :param user_path:续传文件路径
        :return:
        """
        print(os.getcwd())
        file_size = os.stat(file_name).st_size
        with open(file_name, "rb") as f,\
                open(user_path, "ab") as f1:
            pos_size = self.tell_pos(user_path)
            f.seek(pos_size)  # 设置原文件节点
            print("文件断点续传中》》》")
            len_size = pos_size
            for line in f:
                f1.write(line)
                self.m.update(line)
                f1.flush()
                len_size += len(line)
                percent = '{:.2%}'.format(len_size / int(file_size))
                sys.stdout.write("\r")
                sys.stdout.write("[%-100s] %s" % ('=' * (math.floor(len_size / int(file_size) * 100 / 1)), percent))
                #sys.stdout.write("\n")
                sys.stdout.flush()
                time.sleep(0.2)
            print("\n")
            # client_md5_value = self.m.hexdigest()
            # print(client_md5_value)

    def dir_check(self, dir_name, cmd):
        """
        限制用户访问至其他用户的目录
        :param dir_name:用户名
        :param cmd: cmd 命令
        :return:
        """
        path_name = os.path.join(os.path.join(path, "db"), "user")
        os.chdir(path_name)
        result = os.listdir()
        cmd_path = cmd.split()[1]
        print(cmd_path)
        if os.path.exists(cmd_path):
            user_path = re.split("/", cmd_path)
            result.remove(dir_name)
            for i in result:
                if i not in user_path:
                    return True
                else:
                    log_print("没有权限访问他人目录")
                    return False
        else:
            log_print("不是有效文件路径")

    def help_msg(self):
        """
        帮助信息
        :return:
        """
        print("""
        1、get 文件名 下载文件
        2、push 文件名 推送文件
        3、cd 路径    切换目录
        4、ls  查看当前目录下文件 """)

if __name__ == "__main__":
    p = Public()
    p.check_memory("QQ", 2)
    p.dir_check()