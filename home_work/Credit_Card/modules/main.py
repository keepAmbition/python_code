import os
import sys


path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)


from modules.public import date_conversion, week_time, date_time, time_time
from conf.templates import default_menu
from modules.Loging import log_print
from conf.settings import log_file_name
from modules.shopping import choice_goods
from modules.user import user_menu
from modules.credit_card import credit_card_menu
from modules.admin import admin_main_menu
from datebase.date import db_main


def main():
    """
    :return:
    """
    db_main()

    default_func = {
        "1": choice_goods,
        "2": user_menu,
        "3": credit_card_menu,
        "4": admin_main_menu,
        "5": exit
    }
    while True:
        print(default_menu.format(time_time, date_time, week_time))
        choice = input("选择你要进入的功能模块：").strip()
        if choice.isdigit():
            if 0 < int(choice) < 6:
                default_func[choice]()
            else:
                log_print("选择无效请重新输入", log_file_name["operation"])
        else:
            log_print("选择非法请重新输入", log_file_name["operation"])


if __name__ == "main":
    main()