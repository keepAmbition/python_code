import os
import sys
import socket
path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)


from foo.public import Public
from foo.user import login_magic


class ClientSocket(Public):
    ip = "localhost"
    host = 6666

    def __init__(self):
        super(ClientSocket, self).__init__()

    @login_magic
    def client_connect(self):
        client = socket.socket()
        client.connect((ClientSocket.ip, ClientSocket.host))
        while True:
            choice = input("上传 or 下载：")
            if len(choice) == 0:
                continue
            if Public.check_choice(self, choice):
                if choice == "下载":
                    data = client.recv(100000)
                    Public.save_file(self, "from_server", data)
                    print("下载文件内容如下：")
                    print(data.decode())

                elif choice == "上传":
                    data = Public.upload_file(self, "data")
                    client.send(data)
                else:
                    exit()
            else:
                continue
        client.close()

if __name__ == "__main__":
    s = ClientSocket()
    s.client_connect()