import os
import sys
import datetime

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from conf.settings import menu
from foo.public import Public
from log.log_print import log_print
from foo.user import User
from foo.client_socket import ClientSocket
from foo.server_socket import ServerSocket


class Main(object):

    def main(self):
        # 日期
        date_time = datetime.datetime.now().date()
        # 当前时间
        time_time = datetime.datetime.now().strftime("%H:%M:%S")
        menu_dic = {
            '1': User.add_user,
            '2': User.login,
            '3': ClientSocket.client_connect,
            '4': Public.view_directory,
            "5": exit
        }

        while True:
            print(menu.format(time_time, date_time))
            choice = input("请选择：").strip()
            if choice in menu_dic:
                menu_dic[choice](self)
            else:
                log_print("选择无效，请重新选择")


if __name__ == "__main__":
    m = Main()
    m.main()