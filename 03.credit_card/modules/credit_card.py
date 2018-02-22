import os
import sys
import json


path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

from datebase.date_load import load_cl, dumps_cl
from conf.settings import SERVICE_CHARGE, log_file_name
from modules.Loging import log_print
from modules.public import encryption, create_new_id
from conf.templates import ATM_menu
from modules.public import week_time, date_time, time_time


credit_card_tag = False
cl_dict = load_cl()
account = ''

def credit_card_magic(func):
    """
    信用卡装饰器
    """
    def credit_card(*args):
        global credit_card_tag
        if not credit_card_tag:
            global account
            account = input("account:")
            if check_accounts(account):
                password = input("password:")
                if encryption(password) == cl_dict[account]["password"]:
                    credit_card_tag = True
                else:
                    log_print("信用卡%s,密码输入错误！" % account, log_file_name["operation_bill"])
        if credit_card_tag:
            func(*args)
        return account
    return credit_card


@credit_card_magic
def credit_card_menu():
    """
    用户中心
    """
    user_dict = {"1": draw_total,
                 "2": transfer_accounts,
                 "3": repayment,
                 "4": exit
                 }
    while True:
        print(ATM_menu.format(time_time, date_time, week_time))
        user_choice = input("请输入你的选择")
        if user_choice in user_dict:
            user_dict[user_choice](account)
        else:
            log_print("信用卡中心选择菜单无效，请重新选择", log_file_name["operation"])


def pay(total):
    """
    消费结账
    """
    card_number = input("请输入卡号:")
    if check_accounts(card_number):
        password = input("password:")
        if encryption(password) == cl_dict[card_number]["password"]:
            if total <= cl_dict[card_number]["credit_balance"]:
                    balance = cl_dict[card_number]["credit_balance"]-total
                    update_balance(card_number, balance)
                    log_print("信用卡%s,消费%d元,还剩余%d元" % (card_number,total, balance), log_file_name["bill"])
            else:
                log_print("信用卡%s,余额不足" % card_number, log_file_name["operation_bill"])
        else:
            log_print("信用卡密码错误", log_file_name["operation_bill"])
    else:
        exit()


def draw_total(card_number):
    """
    提现
    """
    money = int(input("输入取款金额："))
    if money <= cl_dict[card_number]["credit_balance"]:
        balance = cl_dict[card_number]["credit_balance"]-(money+money * SERVICE_CHARGE)
        update_balance(card_number, balance)
        log_print("提现%d元,还剩余%d元" % (money, balance), log_file_name["bill"])
    else:
        log_print("信用卡%s,提现失败，可提现余额不足" % card_number, log_file_name["operation_bill"])


def transfer_accounts(account1):
    """
    转账
    """
    account2 = input("输入转入的账户：")
    if check_accounts(account2):
        total = int(input("输入转入的金额："))
        account1_balance = cl_dict[account1]["credit_balance"] - total
        account2_balance = cl_dict[account2]["credit_balance"] + total
        update_balance(account1, account1_balance)
        log_print("信用卡%s,余额减少%d元" % (account1, account1_balance), log_file_name["bill"])
        update_balance(account2, account2_balance)
        log_print("信用卡%s,余额增加%d元" % (account2, account2_balance), log_file_name["bill"])



def repayment(account):
    """
    还款
    """
    if check_accounts(account):
        dept = cl_dict[account]["credit_total"]-cl_dict[account]["credit_balance"]
        print("欠款总数为：%d" % dept)

        while True:
            pay_dept = int(input("输入还款金额："))
            if pay_dept == dept:
                new_balance = cl_dict[account]["credit_balance"]+pay_dept
                update_balance(account, new_balance)
                log_print("信用卡%s,成功还款%d元,现在可用余额为%d元" % (account, dept, new_balance), log_file_name["bill"])
                break
            elif pay_dept > dept:
                new_balance = cl_dict[account]["credit_balance"]+pay_dept
                update_balance(account, new_balance)
                log_print("信用卡%s,还款金额%d元，溢出款为%d元" % (account, pay_dept, pay_dept-dept), log_file_name["bill"])
                break
            else:
                log_print("信用卡%s,还款金额不足，还款失败" % account, log_file_name["operation_bill"])


def update_balance(card_number, balance):
    """
    更新账户余额
    """
    cl_db_old = os.path.join(os.path.join(path, "datebase"), "cl.db")
    cl_db_new = os.path.join(os.path.join(path, "datebase"), "cl.db1")
    with open(cl_db_new, "w", encoding="utf-8")as fw:
        cl_dict[card_number]["credit_balance"] = balance
        fw.write(json.dumps(cl_dict))
        fw.flush()
        os.remove(cl_db_old)
        fw.close()
        os.rename(cl_db_new, cl_db_old)


def check_accounts(account):
    """
    检测信用卡是否被锁定或输入非法
    """
    accounts = []
    for k in cl_dict:
        accounts.append(k)
    if len(account) > 0 and account in accounts:
        if cl_dict[account]["status"] != 1:
            return True
        else:
            log_print("信用卡账户被锁定", log_file_name["operation_bill"])
    else:
        log_print("信用卡账户输入为空或不存在", log_file_name["operation_bill"])


def create_new_card():
    """
    增加新的信用卡
    """
    new_id_card = create_new_id()
    card_attribute = {"password": "",
                      "credit_total": 10000,
                      "credit_balance": 10000.0,
                      "owner": "",
                      "status": 0}
    credit_pwd = encryption(input("请输入新信用卡密码："))
    card_attribute["password"] = credit_pwd
    cl_dict.setdefault(new_id_card, card_attribute)
    dumps_cl(cl_dict)
    log_print("新增信用卡成功，信用卡卡号为：%s" % new_id_card, log_file_name["operation_bill"])
    return new_id_card


if __name__ == "__main__":
    credit_card_menu()