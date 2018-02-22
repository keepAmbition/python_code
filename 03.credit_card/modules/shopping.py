import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

from datebase.date_load import load_sl
from modules.user import login_magic_sugar, login_status
from modules.Loging import log_print
from modules.credit_card import pay
from conf.settings import log_file_name
from conf.templates import shopping_menu

sl_dict = load_sl()


@login_magic_sugar
def choice_goods():
    """
    :return:
    """
    # 购物袋
    shopping_bag = []
    # 消费总金额
    shopping_total = 0
    tag = False
    print(shopping_menu)
    while not tag:
        for k in sl_dict:
            print(k, sl_dict[k]["typename"])
        choose = input("选择种类：")
        if choose != "Q":
            if 0 < int(choose) < 4:
                for i in sl_dict[choose]["product"]:
                    print(sl_dict[choose]["product"].index(i), "商品编号：{0},商品名称：{1}，商品价格：{2}".format(i["no"].center(10),
                                                                                                   i["name"].center(10),
                                                                                                   i["price"]))
                choose_one = input("选择第几件商品")
                if choose_one != "Q":
                    if 6 > int(choose_one) >= 0:
                        print(sl_dict[choose]["product"][int(choose_one)]["name"])
                        shopping_bag.append(sl_dict[choose]["product"][int(choose_one)]["name"])
                        shopping_total += sl_dict[choose]["product"][int(choose_one)]["price"]
                        pay(shopping_total)
                        log_print("已购买商品%s,花费%d元" % (sl_dict[choose]["product"][int(choose_one)]["name"],
                                                     sl_dict[choose]["product"][int(choose_one)]["price"]),
                                  log_file_name["shopping"])
                    else:
                        log_print("所选商品不存在", log_file_name["error_shopping"])
                else:
                    tag = True
            else:
                log_print("所选商品种类不存在", log_file_name["error_shopping"])
        else:
            tag = True




if __name__ == "__main__":
    choice_goods()