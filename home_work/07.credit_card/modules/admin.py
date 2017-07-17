import sys
import os
import time

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

from conf.templates import admin_menu
from conf.settings import log_file_name
from datebase.date_load import load_ul, dumps_ul, load_cl, dumps_cl
from modules.public import date_conversion, week_time, date_time, time_time, encryption
from modules.credit_card import create_new_card
from modules.Loging import log_print
from modules.credit_card import check_accounts
from modules.user import judge_account

ul_dict = load_ul()
cl_dict = load_cl()

def judge_admin(func):
    """
    验证是否是管理员账号装饰器
    """
    def judge():
        account = input("输入你的用户名：")
        if judge_account(account):
            if ul_dict[account]["role"] == "admin":
                password = input("请输入密码：")
                if encryption(password) == ul_dict[account]["password"]:
                    func()
                else:
                    log_print("管理员密码错误", log_file_name["operation"])
            else:
                log_print("没有管理员权限", log_file_name["operation"])
    return judge


@judge_admin
def admin_main_menu():
    """
    用户中心
    """
    user_dict = {"1": add_user,
                 "2": promotion_total,
                 "3": locked_account,
                 "4": open_account,
                 "5": exit
                 }
    while True:
        print(admin_menu.format(time_time, date_time, week_time))
        user_choice = input("请输入你的选择")
        if user_choice in user_dict:
            user_dict[user_choice]()
        else:
            log_print("后台管理中心选择菜单无效，请重新选择", log_file_name["operation"])


def add_user():
    """
    添加用户
    """

    new_account = {'password': '',
               'name': '',
               'mobile': '',
               'is_locked': 0,
               'binding_card': '',
               'role': 'user',
               'isdel': 0}

    new_user = input("输入新用户名：")
    password = encryption(input("请输入密码："))
    phone = input(" 请输入电话：")
    new_id_card = create_new_card()
    new_account["name"] = new_user
    new_account["password"] = password
    new_account["mobile"] = phone
    new_account["binding_card"] = new_id_card
    ul_dict.setdefault(new_user, new_account)
    cl_dict1 = load_cl()
    cl_dict1[new_id_card]["owner"] = new_user
    dumps_ul(ul_dict)
    dumps_cl(cl_dict)
    log_print("新增用户%s成功，信用卡卡号为：%s" % (new_user, new_id_card), log_file_name["operation"])


def promotion_total():
    """
    增加用户额度
    """
    account = input("欲提额账户：")
    if check_accounts(account):
        total = int(input("提升金额："))
        new_total = cl_dict[account]["credit_total"] + total
        cl_dict[account]["credit_total"] = new_total
        dumps_cl(cl_dict)
        log_print("提升用户%s额度成功，信用卡卡号为：%s，提升后额度为：%d" % (cl_dict[account]["owner"], account, new_total),  log_file_name["consume"])


def locked_account():
    """
    锁定账户
    """
    account = input("欲锁定账户：")
    if check_accounts(account):
        cl_dict[account]["status"] = 1
        dumps_cl(cl_dict)
        log_print("用户%s，信用卡卡号为：%s，其信用卡已锁定" % (cl_dict[account]["owner"], account), log_file_name["consume"])


def open_account():
    """
    解锁账户
    """
    account = input("欲解锁账户：")
    if check_accounts(account):
        cl_dict[account]["status"] = 0
        dumps_cl(cl_dict)
        log_print("用户%s，信用卡卡号为：%s，其信用卡已解锁" % (cl_dict[account]["owner"], account), log_file_name["consume"])


if __name__ == "__main__":
    admin_main_menu()