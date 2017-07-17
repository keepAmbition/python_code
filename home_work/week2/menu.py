# -*- coding:utf-8 -*-
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                '优酷': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}
Exit = "T"
while Exit != "Q":
    for i in menu:
        print(i)

    select = input("选择1级菜单：")
    if select in menu:
        while Exit != "Q":
            for i1 in menu[select]:
                print(i1)
            select2 = input("选择2级菜单：")
            if select2 in menu[select]:
                while Exit != "Q":
                    for i2 in menu[select][select2]:
                        print(i2)
                    select3 = input("选择3级菜单：")
                    if select3 in menu[select][select2]:
                        while Exit != "Q":
                            for i4 in menu[select][select2][select3]:
                                print(i4)
                            select4 = input("返回上一页或者退出")
                            if select4 == "B":
                                break
                            elif select4 == "Q":
                                Exit = "Q"

                    elif select3 == "Q":
                        Exit = "Q"
                    if select3 == "B":
                        break
            elif select2 == "Q":
                Exit = "Q"

            if select2 == "B":
                break
    elif select == "Q":
        Exit = "Q"