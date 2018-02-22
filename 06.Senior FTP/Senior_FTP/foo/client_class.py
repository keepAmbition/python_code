import socket
import os
import sys
import hashlib
import time
import math


path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)


from log.log_print import log_print
from foo.user_class import User
from foo.public_class import Public


class Client(Public):

    def __init__(self):
        self.HOST = "localhost"
        self.PORT = 6666
        self.client = socket.socket()
        Public.__init__(self)

    #@login_magic
    def client_connect(self):
        """
        客户端连接服务端函数，负责用户登陆，cmd命令输入
        :return:
        """
        u = User("AA", "AA", "AAA")
        dir_name = u.login()
        # print(dir_name)
        self.client.connect((self.HOST, self.PORT))
        while True:
            cmd = input("cmd:>>>>").strip()
            print(cmd)
            if len(cmd) == 0:
                continue
            command_line = ["cd", "ls", "get", "push"]
            if cmd.split()[0] in command_line:
                if cmd.startswith("cd"):
                    if Public.dir_check(self, dir_name, cmd):
                        self.client.send(cmd.encode())
                        self.cmd_parsing(cmd, dir_name)
                else:
                    self.client.send(cmd.encode())
                    self.cmd_parsing(cmd, dir_name)
            else:
                log_print("无效命令")

    def cmd_parsing(self, cmd, dir_name):
        """
        cmd 命令的解析函数
        :param cmd: 命令 如 ls,cd
        :param dir_name:用户目录名 如QQ,QQ1
        :return:
        """
        if cmd.startswith("get"):
            self.get_data(cmd, dir_name)
        elif cmd.startswith("push"):
            self.push_data(cmd)
        elif cmd.startswith("cd"):
            self.cd_dir()
        else:
            self.ls_file()

    def get_data(self, cmd, dir_name):
        """
        客户端get命令的功能实现
        :param cmd: 命令
        :param dir_name: 用户目录名
        :return:
        """
        # 接收服务端当前文件路径
        path_path = self.client.recv(1024)
        file_name = cmd.split()[1]  # 文件名
        user_path = os.path.join(os.path.join(os.path.join(os.path.join(path, "db"), "user"), dir_name),
                                 file_name + "_new")
        if not os.path.exists(user_path):
            self.client.send("开始下载文件".encode())
            if os.path.exists(user_path):
                file_size = self.client.recv(1024)  # 接收文件大小
                if Public.check_memory(self, dir_name, math.floor(int(file_size.decode()) / 1024)):
                    print("即将接收数据大小:", file_size.decode())
                    self.client.send("客户准端备好接收数据内容了".encode())
                    revived_size = 0
                    file_size = file_size.decode()
                    m = hashlib.md5()  # 生成MD5对象,不能把 MD5实例放在类静态变量里面,（self.m = hashlib.md5()）不然MD5值 会始终累加。
                    user_path = os.path.join(os.path.join(os.path.join(os.path.join(path, "db"), "user"), dir_name),
                                             file_name + "_new")
                    with open(user_path, "wb") as f:
                        while revived_size < int(file_size):
                            if int(file_size) - revived_size > 1024:  # 只要剩余文件字节大于1024字节，就默认最大值接收
                                size = 1024
                            else:
                                size = int(file_size) - revived_size   # 最后一次，剩多少收多少
                                #print("last receive:", size)
                            file_data = self.client.recv(size)
                            revived_size += len(file_data)
                            m.update(file_data)  # 不断更新计算接收数据的文件值
                            percent = '{:.2%}'.format(revived_size / int(file_size))
                            sys.stdout.write("\r")
                            sys.stdout.write("[%-100s] %s" % ('=' * (math.floor(revived_size / int(file_size) * 100 / 1))
                                                              , percent))
                            #sys.stdout.write("\n")
                            sys.stdout.flush()
                            time.sleep(0.5)

                            f.write(file_data)
                            f.flush()
                        else:

                            #print("\n文件大小对比:", file_size, revived_size)
                            client_md5_value = m.hexdigest()  # 生成接收数据的MD5值16进制形式
                        server_md5_value = self.client.recv(1024)  # 接收服务端的MD5值
                        self.client.send(client_md5_value.encode())
                        #print("client:%s，server:%s" % (client_md5_value, server_md5_value.decode()))
                        if client_md5_value == server_md5_value.decode():
                            print("\nmd5值一致，校验通过")
                        else:
                            print("校验不通过")
            else:
                log_print("文件不存在")
        else:
            self.client.send("断点续传中".encode())
            Public.check_breakpoint(self, os.path.join(path_path.decode(), cmd.split()[1]), user_path)

    def push_data(self, cmd):
        """
        客户端push命令功能实现
        :param cmd: 命令
        :return:
        """
        #当前服务端的实时目录
        path_path = self.client.recv(1024)
        user_path = os.path.join(os.path.join(os.path.join(path, "db"), "server_save_file"),
                                 cmd.split()[1] + "_new")
        if not os.path.exists(user_path):
            self.client.send("开始上传文件".encode())

            number = 0
            file_name = cmd.split()[1]
            m = hashlib.md5()   # 生成MD5对象,不能把 MD5实例放在类静态变量里面,（self.m = hashlib.md5()）不然MD5值 会始终累加。
            # 接收服务端实时切换的位置
            dir_path = os.path.join(path_path.decode(), file_name)
            if os.path.exists(dir_path):
                with open(dir_path, "rb")as f:
                    file_size = os.stat(dir_path).st_size
                    self.client.send(str(file_size).encode())
                    print("即将上传的文件大小为:%sM" % math.floor(file_size / 1024))
                    mag = self.client.recv(1024)
                    print(mag.decode())
                    for line in f:
                        number += len(line)
                        m.update(line)
                        self.client.send(line)
                        percent = '{:.2%}'.format(number / file_size)
                        sys.stdout.write("\r")
                        sys.stdout.write("[%-100s] %s" % ('=' * (math.floor(number / file_size
                                                                            * 100 / 1)), percent))
                        sys.stdout.flush()
                        # sys.stdout.write("\n")
                        time.sleep(0.2)
                    # print("\nmd5值", m.hexdigest())
                self.client.send(m.hexdigest().encode())
                data = self.client.recv(1024)
                print("\n", data.decode())
            else:
                log_print("文件%s不存在" % file_name)
        else:
            self.client.send("断点续传中".encode())
            Public.check_breakpoint(self, os.path.join(path_path.decode(), cmd.split()[1]), user_path)

    def cd_dir(self):
        """
        cd 命令实现
        :return:
        """
        result = self.client.recv(1024)
        print(result.decode())
        # result1 = self.client.recv(1024)
        # print(result1.decode())

    def ls_file(self):
        """
        ls 命令实现
        :return:
        """
        print("当前目录下文件：")
        file = self.client.recv(1024)
        for i in eval(file.decode()):
            print(i)


if __name__ == "__main__":
    c = Client()
    c.client_connect()