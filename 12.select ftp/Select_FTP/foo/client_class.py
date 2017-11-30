import os
import sys
import socket
import time
import random
import string

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from log.log_print import log_print


class Client(object):

    def __init__(self, host="localhost", port=8888):
        self.host = host
        self.port = port
        self.client = socket.socket()

    def client_connect(self):
        """
        连接服务端
        :return:
        """
        self.client.connect((self.host, self.port))
        while True:
            cmd = input("cmd>>>>>").strip()
            if len(cmd) == 0:
                continue
            command_line = ["get", "put", "exit"]
            if cmd.split()[0] in command_line:
                if cmd.split()[0] == "exit":
                    break
                else:
                    self.client.send(cmd.encode())
                    self.cmd_parsing(cmd)
            else:
                log_print("无效命令")

    def cmd_parsing(self, cmd):
        """
        cmd 命令的解析函数
        :param cmd: 命令 如 get put
        :return:
        """
        if cmd.startswith("get"):
            self.get_file(cmd)
        else:
            self.put_file(cmd)

    def get_file(self, cmd):
        """
        客户端get命令的功能实现
        :param cmd: 命令
        :return:
        """
        now = "".join(random.sample(string.ascii_uppercase, 5))
        path_path = self.client.recv(1024)
        file_name = cmd.split()[1]
        file_path = os.path.join(path_path.decode(), file_name)
        if os.path.exists(file_path):
            file_size = self.client.recv(1024)
            revived_size = 0
            file_size = file_size.decode()
            save_path = os.path.join(os.path.join(os.path.join(path, "db"), "save_get_file"), file_name + "--" + now)
            with open(save_path, "wb") as f:
                while revived_size < int(file_size):
                    if int(file_size) - revived_size > 1024:
                        size = 1024
                    else:
                        size = int(file_size) - revived_size
                    file_data = self.client.recv(size)
                    revived_size += len(file_data)
                    f.write(file_data)
                    f.flush()
            log_print("文件下载成功")
        else:
            log_print("文件不存在")

    def put_file(self, cmd):
        """
        客户端put命令功能实现
        :param cmd: 命令
        :return:
        """
        file_name = cmd.split()[1]
        if os.path.exists(file_name):
            with open(file_name, "rb")as f:
                time.sleep(0.5)
                for line in f:
                    self.client.send(line)
            log_print("文件上传成功")
        else:
            log_print("文件%s不存在" % file_name)

if __name__ == "__main__":
    client = Client()
    client.client_connect()