# -*- coding: utf-8 -*-
import os
import sys
import socket

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)


from foo.public import Public
from log.log_print import log_print


class ServerSocket(Public):
    ip = "localhost"
    host = 6666

    def __init__(self):
        super(ServerSocket, self).__init__()

    def server_connect(self):
        server = socket.socket()
        server.bind((ServerSocket.ip, ServerSocket.host))
        server.listen()
        conn, address = server.accept()
        print("连接成功")
        while True:
            send_data = Public.upload_file(self, "data")
            conn.sendall(send_data)
            data = conn.recv(10000)
            Public.save_file(self, "from_client", data)
            print("上传文件内容如下：")
            print(data.decode())
        server.close()


if __name__ == "__main__":
    s = ServerSocket()
    s.server_connect()