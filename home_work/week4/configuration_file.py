import os
def select_file(select_str):
    # 查
    string = "backend "+select_str
    line_list = []
    for line in f:
        line_list.append(line.strip())
    print("查询成功："+str((line_list[line_list.index(string)+1:])))



def change_file(change_str):
    # 改
    dict1 = change_str
    dict1 = eval(dict1)
    list_str = []
    backend = "backend "+dict1["backend"]
    a = dict1["record"]
    for k in a:
        list_str.append(k)
        list_str.append(a[k])
    line_str = " ".join(list_str)
    for line in f:
        if line.startswith("backend"):
            line = line.replace(line, backend)
        if line.lstrip().startswith("server"):
            line = line.replace(line, "\n\t\t"+line_str)
            print("修改成功，请在file文件中查看")
        f1.write(line)
        f1.flush()


def delete_file(delete_str):
    # 删
    dict1 = delete_str
    dict1 = eval(dict1)
    list_str = []
    backend = "backend "+dict1["backend"]
    a = dict1["record"]
    for k in a:
        list_str.append(k)
        list_str.append(a[k])
    line_str = " ".join(list_str)
    for line in f:
        f1.write(line)
        f1.flush()
        if backend and line_str in line:
            print("删除成功，请在file文件中查看")
            break



def update_file(update_str):
    # 增
    dict1 = update_str
    dict1 = eval(dict1)
    line_list = []
    list_str = []
    backend = "backend "+dict1["backend"]
    a = dict1["record"]
    for line in f:
        line_list.append(line.strip())
    for k in a:
        list_str.append(k)
        list_str.append(a[k])
    line_str = " ".join(list_str)

    if backend not in line_list:
        print("backend不存在,增添backend和record")
        line_list1 = ("\n".join(line_list))
        f1.write(line_list1)
        f1.write(backend)
        f1.write("\n\t\t"+line_str)
        f1.flush()
        print("backend和record增添成功，请在haproxy文件中查看")
    elif line_str != line_list[-1]:
        print("record中的信息不一致，修改IP")
        line_list1 = ("\n\t".join(line_list[:-1]))
        f1.write(line_list1)
        line_list[-1] = line_str
        f1.write("\n\t\t"+line_list[-1])
        f1.flush()
        print("IP修改成功，请在file文件中查看")
    else:
        print("record中的信息一致，不作操作")


filename = r"C:\Users\dell\PycharmProjects\untitled\home_work\week4\haproxy"
if os.path.exists(filename):
    with open("haproxy", "r+", encoding="utf-8")as f,\
            open("file", "r+", encoding="utf-8")as f1:
        menu = ["退", "增", "删", "查", "改"]
        while True:
            for i in menu:
                print(menu.index(i), i)
            choice = input("请选择相应操作：")
            if choice.isdigit():
                choice = int(choice)
                if choice<len(menu) and choice >=0:
                    if choice == 0:
                        print("再见".center(50, "-"))
                        exit()
                    elif choice == 1:
                        update_str = input("请输入你要添加的内容：")
                        update_file(update_str)
                        break
                    elif choice == 2:
                        delete_str = input("请输入你要删除的内容：")
                        delete_file(delete_str)
                        break
                    elif choice == 3:
                        select_str = input(" 请输出你要查询的内容：")
                        select_file(select_str)
                        break
                    else:
                        change_str = input("请输入你要修改的内容：")
                        change_file(change_str)
                        break
                else:
                    print("无效输入，请重新输入")

            else:
                print("无效输入，请重新输入")
else:
    print("文件不存在")