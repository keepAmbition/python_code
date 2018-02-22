import os
import json
import sys
# 不添加当前文件目录进入环境变量，导入conf，modules 会报错找不到其文件
PATH_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH_DIR)

from conf import settings
from modules import public,Loging
# 商品清单
shopping_list = {
    "1": {"typename": "食品生鲜", "product": (
        {"no": "0001", "name": "樱桃", "price": 95},
        {"no": "0002", "name": "安慕希", "price": 79},
        {"no": "0003", "name": "费列罗巧克力", "price": 205},
        {"no": "0004", "name": "阳澄湖大闸蟹", "price": 458},
        {"no": "0005", "name": "三只松鼠", "price": 168},
        {"no": "0006", "name": "北海道饼干", "price": 256}
    )},
    "2": {"typename": "数码产品", "product": (
        {"no": "1001", "name": "佳能（Canon）", "price": 9326},
        {"no": "1002", "name": "phone6", "price": 4000},
        {"no": "1003", "name": "小米6s", "price": 2499},
        {"no": "1004", "name": "华为", "price": 3999},
        {"no": "1005", "name": "魅族 香槟金 32G ", "price": 2468},
        {"no": "1006", "name": "Apple MacBook Air ", "price": 6988}
    )},
    "3": {"typename": "男装女装", "product": (
        {"no": "2001", "name": "连衣裙", "price": 163},
        {"no": "2002", "name": "Maxchic长袖", "price": 235},
        {"no": "2003", "name": "牛仔裤", "price": 169},
        {"no": "2004", "name": "羽绒服", "price": 319},
        {"no": "2005", "name": "猿人头袖", "price": 298},
        {"no": "2006", "name": "套头卫衣 ", "price": 159}
    )}
}
# 用户信息
user_list = {
        "test": {"password": "6666", "name": "test", "mobile": "13511111111", "is_locked": 0, "binding_card": "1001012345",
             "role": "user"},
    "admin": {"password": "8888", "name": "admin", "mobile": "15257157418", "is_locked": 0, "binding_card": "1001010002",
              "role": "admin"}
}
# 信用卡信息
credit_card_list = {
    "1001012345": {"password": "12345", "credit_total": 10000, "credit_balance": 10000,
                   "owner": "test", "status": 0},
    "1001010002": {"password": "12345", "credit_total": 10000, "credit_balance": 10000,
                   "owner": "admin", "status": 0}
}
# 表名 sl.db 是购物商品清单表  ul.db 是用户信息表 cl.db 是信用卡信息表
tables = ["sl.db", "ul.db", "cl.db"]


def db_shopping_list():
    """
    生成商城数据表
    :return:
    """
    ab_path = os.path.join(settings.DATABASE["dbpath"], "sl.db")
    with open(ab_path, "w+", encoding="utf-8")as f:
        f.write(json.dumps(shopping_list))


def db_user_list():
    """
    生成用户信息数据表
    :return:
    """
    ab_path = os.path.join(settings.DATABASE["dbpath"], "ul.db")
    with open(ab_path, "w+", encoding="utf-8")as f:
        for key in user_list:
            pwd = user_list[key]["password"]
            encryption_pwd = public.encryption(pwd)
            user_list[key]["password"] = encryption_pwd
        f.write(json.dumps(user_list))
        f.flush()


def db_credit_list():
    """
    # 生成信用卡信息数据表
    :return NULL
    """
    ab_path = os.path.join(settings.DATABASE["dbpath"], "cl.db")
    with open(ab_path, "w+", encoding="utf-8")as f:
        for key in credit_card_list:
            pwd = credit_card_list[key]["password"]
            encryption_pwd = public.encryption(pwd)
            credit_card_list[key]["password"] = encryption_pwd
        f.write(json.dumps(credit_card_list))


def db_main():
    """
    运行此函数可分别生成用户信息表、信用卡信息表、商城信息表
    :return:
    """
    funcs = ["db_shopping_list", "db_user_list", "db_credit_list"]
    path = settings.DATABASE["dbpath"]
    for table in tables:
        if not os.path.exists(os.path.join(path, table)):
            print("创建表%s成功" % table)
            for i in funcs:
                if hasattr(sys.modules[__name__], i):
                    func = getattr(sys.modules[__name__], i)
                    func()
        else:
            Loging.log_print("创建表%s失败" % table, settings.log_file_name["operation"])

if __name__ == "__main__":
    db_main()
