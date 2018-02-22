import os
import sys
import select
import socket
import queue


path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from log.log_print import log_print


class Server():

    def __init__(self, host="localhost", port=8888):
        self.host = host
        self.port = port
        self.mes_dic = dict()
        self.up_file_name = ""
        self.down_file_name = ""
        self.address = ''

    def server_connect(self):
        """
        连接客户端
        :return:
        """
        server_server = socket.socket()
        server_server.bind((self.host, self.port))
        server_server.listen(100)
        server_server.setblocking(False)
        inputs = [server_server, ]
        outputs = []
        while True:
            readable, writeable, exceptional = select.select(inputs, outputs, inputs)
            for i in readable:
                if i is server_server:
                    conn, address = i.accept()
                    print("建立新链接", address)
                    self.address = address
                    inputs.append(conn)
                    self.mes_dic[conn] = queue.Queue()
                else:
                    data = i.recv(1024)
                    if data:
                        try:
                            data = data.decode()
                            if data.split()[0] == "get":
                                self.down_file_name = data.split()[1]
                                self.get_file(i)
                            elif data.split()[0] == "put":
                                self.up_file_name = data.split()[1]
                            else:
                                self.put_file(data)
                            if i not in outputs:
                                outputs.append(i)
                        except UnicodeDecodeError as e:
                            log_print(e)
                    else:
                        if i in outputs:
                            outputs.remove(i)
                        inputs.remove(i)
                        i.close()

            for w in writeable:
                try:
                    self.mes_dic[w].get_nowait()
                except queue.Empty:
                    outputs.remove(w)

            for e in exceptional:
                if e in outputs:
                    outputs.remove(e)
                inputs.remove(e)
                del self.mes_dic[e]

    def get_file(self, i):
        """
        服务端将指定的下载文件发送给客户端
        :param i: conn 客户端实例
        :return:
        """
        i.send(os.getcwd().encode())
        if os.path.exists(self.down_file_name):
            with open(self.down_file_name, "rb")as f:
                file_size = os.stat(self.down_file_name).st_size
                i.send(str(file_size).encode())
                for line in f:
                    i.send(line)
        else:
            log_print("文件不存在%s" % self.down_file_name)

    def put_file(self, data):
        """
        将客户端上传至服务端的文件保存至指定路径
        :param data 客户端上传至服务端的数据
        :return:
        """
        file_path = os.path.join(os.path.join(os.path.join(path, "db"), "server_save_file"), self.up_file_name + "%s" % self.address[1])
        with open(file_path, "ab") as f:
            f.write(data.encode())

if __name__ == "__main__":
    server = Server()
    server.server_connect()