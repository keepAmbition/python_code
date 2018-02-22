import os
import sys
import datetime

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from foo.user_class import User
from foo.client_class import Client
from conf.templates import menu
from foo.public_class import Public
from log.log_print import log_print


class Main(User, Client):
    def __init__(self):
        super(Main, self).__init__("as", "adds", "ads")
        Client.__init__(self)

    def main(self):
        # 日期
        date_time = datetime.datetime.now().date()
        # 当前时间
        time_time = datetime.datetime.now().strftime("%H:%M:%S")
        menu_dic = {
            '1': User.register,
            '2': User.login,
            '3': Client.client_connect,
            '4': Public.help_msg,
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