# -*- coding:utf-8 -*-
count = 0
with open("file", "r")as f,\
        open("file2", "r+")as f2:
    user_n = f.readline().strip()
    password = f.readline().strip()
    user = input("请输入用户名：")
    if user not in f2:
        if user == user_n:
            while count < 3:
                pwd = input("请输入密码：")
                if pwd != password:
                    count += 1
                    print("密码错误，你还剩下%s次机会" % (3-count))
                    if count == 3:
                        f2.write(user_n)
                        print("账号被锁定")
                else:
                    print("登录成功")
                    break
        else:
            print("用户不存在")
    else:
        print("账号被限制")