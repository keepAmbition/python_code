import os
import sys
import socketserver
import hashlib

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from foo.public_class import Public
from log.log_print import log_print


class MyServer(socketserver.BaseRequestHandler, Public):
    def handle(self):
        while True:
            try:
                data = self.request.recv(1024)  # 服务端接受数据
                log_print("{0} write:".format(self.client_address[0]))  # 打印客户端地址
                print(data)
                self.cmd_parsing(data.decode())
                #self.request.send(data.upper())  # 将客户端接收到数据大写后再发送回去
            except ConnectionResetError as e:
                print("error:", e)
                break

    def cmd_parsing(self, data):
        """
        cmd 命令解析
        :param data: cmd 命令
        :return:
        """
        if data.startswith("get"):
            cmd, file_name = data.split()
            log_print("执行指令:%s, 文件名:%s" % (cmd, file_name))
            self.get_data(file_name)
        elif data.startswith("push"):
            cmd, file_name = data.split()
            log_print("执行指令:%s, 文件名:%s" % (cmd, file_name))
            self.push_data(file_name)
        elif data.startswith("cd"):
            cmd, path_name = data.split()
            log_print("执行指令:%s, 路径:%s" % (cmd, path_name))
            self.cd_dir(path_name)
        else:
            log_print("执行指令: ls")
            self.ls_file()

    def get_data(self, file_name):
        """
        服务端get命令实现
        :param file_name: 文件名
        :return:
        """
        m = hashlib.md5()
        # 发送当前程序所在目录路径
        self.request.send(os.getcwd().encode())
        client_msg = self.request.recv(1024)
        if client_msg.decode() != "断点续传中":
            if os.path.exists(file_name):
                log_print(client_msg.decode())
                with open(file_name, "rb")as f:
                    file_size = os.stat(file_name).st_size
                    self.request.send(str(file_size).encode())
                    print("即将发送的文件大小为：", file_size)
                    self.request.recv(1024)
                    for line in f:
                        m.update(line)
                        self.request.send(line)
                    print("md5值", m.hexdigest())
                self.request.send(m.hexdigest().encode())
                client_md5_value = self.request.recv(1024)
                if m.hexdigest == client_md5_value.decode():
                    log_print("文件传输完成，未使用断点续传功能")
            else:
                log_print("文件不存在%s" % file_name)
        else:
            log_print(client_msg.decode())

    def push_data(self, file_name):
        """
        服务端push命令实现
        :param file_name:文件名
        :return:
        """
        m = hashlib.md5()
        #发送当前程序所在目录
        self.request.send(os.getcwd().encode())
        client_msg = self.request.recv(1024)
        if client_msg.decode() != "断点续传中":
            print(client_msg.decode())
            if os.path.exists(file_name):
                self.request.send("服务端准备好接收数据内容了".encode())
                file_size = self.request.recv(1024)
                print("即将接收数据大小:", file_size.decode())
                #self.request.send("服务端正式接收数据".encode())
                revived_size = 0
                # 服务器
                file_path = os.path.join(os.path.join(os.path.join(path, "db"), "server_save_file"), file_name + "_new")
                with open(file_path, "wb") as f:
                    while revived_size < int(file_size.decode()):
                        if int(file_size.decode()) - revived_size > 1024:
                            size = 1024
                        else:
                            size = int(file_size.decode()) - revived_size
                            print("last receive:", size)
                        revived_data = self.request.recv(size)
                        revived_size += len(revived_data)
                        m.update(revived_data)
                        f.write(revived_data)
                    else:
                        print(file_size, revived_size)
                        server_md5_value = m.hexdigest()  # 生成接收数据的MD5值16进制形式
                    client_md5_value = self.request.recv(1024)  # 接收服务端的MD5值
                    print("client:%s，server:%s" % (client_md5_value.decode(), server_md5_value))
                    if server_md5_value == client_md5_value.decode():
                        self.request.send("md5值一致，校验通过".encode())
                    else:
                        self.request.send("校验不通过".encode())
            else:
                log_print("文件不存在")

        else:
            log_print(client_msg.decode())

    def cd_dir(self, path_name):
        """
        cd 命令实现
        :param path_name: 路径
        :return:
        """
        if os.path.exists(path_name):
            os.chdir(path_name)
            self.request.send(("目录已切换至: %s" % os.getcwd()).encode())
        else:
            self.request.send("文件路径不存在".encode())

    def ls_file(self):
        """
        ls 命令实现
        :return:
        """
        result = os.listdir()
        print(result)
        self.request.send(str(result).encode())


if __name__ == "__main__":
    HOST, PORT = "localhost", 6666
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyServer)  # 采用ForkingTCPServer多线程方式实例化
    server.serve_forever()  # 实现多个链接
    server.server_close()   # 关闭socket server
