import sys
import os
import json


path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)


from conf.settings import log_file_name
from datebase.date_load import load_ul, dumps_ul
from modules.public import date_conversion, week_time, date_time, time_time, encryption
from modules import Loging
from conf.templates import user_templates, report_bill, shopping_history, user_center


ul_dict = load_ul()
login_status = False


def login_magic_sugar(func):
    """
    用户装饰器
    """
    def magic_inner(*args):
        global login_status
        if not login_status:
            login_check()
        if login_status:
            func(*args)
    return magic_inner


@login_magic_sugar
def user_menu():
    """
    用户中心
    """

    user_dict = {"1": update_pwd,
                 "2": my_bill,
                 "3": my_shopping_list,
                 "4": my_date,
                 "5": exit
                 }
    while True:
        print(user_center.format(time_time, date_time, week_time))
        user_choice = input("请输入你的选择")
        if user_choice in user_dict:
            user_dict[user_choice]()
        else:
            Loging.log_print("用户中心选择菜单无效，请重新选择", log_file_name["operation"])



def update_pwd():
    """
    修改密码
    """
    account = input("请输入你的账号：")
    if judge_account(account):
        new_pwd = input("请输入你的新密码")
        ul_dict[account]["password"] = new_pwd
        dumps_ul(ul_dict)
        Loging.log_print("密码修改成功", log_file_name["operation"])

def my_bill():
    """
    查看账单
    """
    print(report_bill.format(time_time, date_time, week_time))
    bill_path = os.path.join(os.path.join(path, "log"), log_file_name["bill"])
    if os.path.exists(bill_path):
        with open(bill_path, "r", encoding="utf-8")as f:
            for line in f:
                print(line[43:])


def my_shopping_list():
    """
    查看消费历史
    """
    print(shopping_history.format(time_time, date_time, week_time))
    bill_path = os.path.join(os.path.join(path, "log"), log_file_name["shopping"])
    if os.path.exists(bill_path):
        with open(bill_path, "r", encoding="utf-8")as f:
            for line in f:
                print(line[43:])


def my_date():
    """
     查看个人资料
    """
    name = input("请输入你的账号：")
    print(user_templates.format(ul_dict[name]["name"], ul_dict[name]["mobile"], ul_dict[name]["role"],
                                ul_dict[name]["is_locked"], ul_dict[name]["binding_card"]))


def login_check():
    """
    对登陆的账号和密码进行检查; 密码输错三次进行锁定操作
    """
    global login_status
    count = 0
    user_name = input("name:").strip()
    if judge_account(user_name):
        while count < 3:
            password = input("password:").strip()
            if len(password) > 0:
                if encryption(password) == ul_dict[user_name]["password"]:
                    Loging.log_print("用户%s登陆成功" % user_name, log_file_name["operation"])
                    login_status = True
                    return login_status, user_name
                else:
                    count += 1
                    if count == 3:
                        Loging.log_print("密码输入次数过多，账号被锁定", log_file_name["operation"])
                        break
                    Loging.log_print("密码错误，你还剩下%d次机会" % (3-count), log_file_name["operation"])

            else:
                Loging.log_print("密码为空", log_file_name["operation"])
        else:
            islocked(user_name)



def islocked(user_name):
    """
    :param user_name 传入要被锁定的用户名
    :return null
    """
    ul_db_old = os.path.join(os.path.join(path, "datebase"), "ul.db")
    ul_db_new = os.path.join(os.path.join(path, "datebase"), "ul.db1")
    with open(ul_db_new, "w", encoding="utf-8")as fw:
        ul_dict[user_name]["is_locked"] = 1
        fw.write(json.dumps(ul_dict))
        fw.flush()
        os.remove(ul_db_old)
        fw.close()
        os.rename(ul_db_new, ul_db_old)


def judge_account(account):
    """
    判断账户合法性
    """
    names = []
    for k in ul_dict:
        names.append(ul_dict[k]["name"])
    if len(account) > 0:
        if account in names:
            if int(ul_dict[account]["is_locked"]) != 1:
                return True
            else:
                Loging.log_print("账号已被锁定", log_file_name["operation"])
        else:
            Loging.log_print("账户不存在", log_file_name["operation"])
    else:
        Loging.log_print("用户名为空", log_file_name["operation"])

if __name__ == "main":
    user_menu()