# -*- coding:utf-8 -*-
# 定义商品列表
commodity = [("iphone4", 2000), ("iphone5", 3000), ("iphone6", 4000), ("iphone6s", 5000), ("iphone7", 7000)]
# 上次购买商品清单
commodity_list = []
# 已购买商品清单
purchase_list = []

def shopping(salary):
    while True:
        # 为商品增加编号，并展示商品
        for i in commodity:
            print(commodity.index(i), i)
        choice = input("请输入你要购买的商品列表：")
        if choice.isdigit():
            choice = int(choice)
            if choice < len(commodity) and choice >= 0:
                # 选择购买的商品
                goods = commodity[choice]
                # 如果购买的商品价格小于或者等于工资，就扣款，并把商品增加到已购商品列表
                if goods[1] <= salary:
                    purchase_list.append(goods[0])
                    # 工资减去商品价格，还剩下的工资
                    salary -= goods[1]
                    print("\033[42;1m添加%s至购物车，余额还剩%d\033[0m" % (goods[0], salary))
                else:
                    print("\033[42;1m余额不足\033[0m")
            else:
                print("商品不存在")
        elif choice == "Q":
            print("------------------")
            # int 类型写入报错
            f1.write(str(salary))
            for j in purchase_list:
                print(j)
                f1.write("\n"+j)
                f1.flush()
            print("余额%d" % salary)

            f.write(user)
            f.write("\n"+pwd)
            f.flush()
            exit()


with open("file", "r+")as f,\
        open("file1", "r+")as f1:
    user = input("请输入用户名：")
    pwd = input("请输入密码：")
    if user and pwd not in f:
        salary = input("请输入工资：")
        if salary.isdigit():
            salary = int(salary)
            shopping(salary)
        else:
            print("无效输入")
    else:
        select = input("是否查询上一次购买商品")
        if select == "Y":
            for i in f1:
                commodity_list.append(i.strip())
            print(commodity_list[1:])
        else:
            salary = int(f1.readline())
            shopping(salary)
