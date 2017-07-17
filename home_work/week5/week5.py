import os
def sql_action(sql_list):
    """
    把解析好sql语句，根据关键字分别交给指定函数处理
    :param sql_list :用户输入的sql语句解析成列表形式
    """

    if sql_list[0] == "select":
        sql_dict = sql_parse(sql_list)
        final = select(sql_dict)
        for i in final:
            print(i)
    elif sql_list[0] == "update":
        update(sql_list)
    elif sql_list[0] == "delete":
        delete(sql_list)
    else:
        insect(sql_list)


def sql_parse(sql):
    """
    该函数的功能是将列表中的内容对号入座的放到相应的字典当中
    :param sql: 用户传进来的列表形式的数据
    :return: sql_dict数据
    """
    sql_dict = {
        "select": [],
        "from": [],
        "where": [],
        "limit": [],
        "values": []
    }
    # 状态警报
    tag = False
    key = ""
    # ['select', 'name,age', 'from', 'staff_table', 'where', 'age', '>', '22']
    # 循环sql_list如警报拉响，且sql列表的key在sql字典中，关闭警报
    for i in sql_list:
        if tag and i in sql_dict:
            tag = False
        # 如果警报没有拉响，拉响警报，i就是sql_dict的key，结束此次循环
        if not tag and i in sql_dict:
            tag = True
            key = i
            continue
        # 警报拉响时，且没有满足上面两个条件，此时i就是value
        if tag:
            sql_dict[key].append(i)

    return sql_dict


def delete(sql):
    """
    :param sql 列表形式的sql 语句
    :return 返回删除结果
    """
    table_name = sql[2]
    table_bak = sql[2]+"1"
    # 欲删除的id 和id值
    id, value = sql[4], sql[-1]
    count = 0
    title = "id,name,age,phone,dept,enroll_date"
    with open("%s" % table_name, "r", encoding='utf-8') as fr,\
            open("%s" % table_bak, "w", encoding='utf-8') as fw:
            for line in fr:
                dic = dict(zip(title.split(","), line.strip().split(",")))
                if dic[id] == value:
                    count += 1
                else:
                    fw.write(line)
                    fw.flush()
            # 文件需要关闭，才能进行重命名或者删除任务，不然会报错
            fr.close()
            os.remove("%s" % table_name)
            fw.close()
            os.rename("%s" % table_bak, "%s" % table_name)
            return print("删除成功，共有%s行被删除" % count)

def insect(sql):
    """
    此函数用于处理新增的value值
    :param sql :列表形式的sql语句
    :return 返回新增value值的次数
    """
    # 解析表名 和利用函数 sql_parse()将sql list转换成sql dict
    table_name = sql[2]
    sql_dict = sql_parse(sql)
    count = 0
    with open("%s" % table_name, "r+", encoding='utf-8') as fr:
        f_list = fr.readlines()
        # 利用生成器返回电话信息列表
        phone_list = [j.strip().split(',')[3] for j in f_list]
        if not f_list:
            new_id = 1
        else:
            # 获取最后id值+1，即新value值的id
            last_id = f_list[-1].split(",")
            new_id = int(last_id[0])+1
            # 获取values值列表
        values = sql_dict.get("values")
        values = ''.join(values).split("/")
        for i in values:
            if i .split(",")[2] in phone_list:
                print("手机号%s重复,无法添加%s进入数据库" % (i.split(",")[2], i.split(",")[0]))
            else:
                new_line = "\n%s,%s" % (str(new_id), i)
                new_id += 1
                fr.write(new_line)
                fr.flush()
                count += 1
        return print("新增成功，共插入%d条数据" % count)
def update(sql):
    """
    :param sql 列表形式的的SQL语句
    :return 返回更新结果
    """
    count = 0
    table_name = sql_list[1]
    table_bak = sql_list[1]+"1"
    # set 值['dept=Market', 'phone=13566677787']
    values = sql_list[3].split(",")
    tittle = "id,name,age,phone,dept,enroll_date"
    # 去除=，变成[['dept', 'Market'], ['phone', '13566677787']]
    set_values = [i.split("=") for i in values]
    # 利用 sql_prase()函数把sql列表变成字典类型，最终变成列表套列表[['id', '=', '2']]进行True,False逻辑判断
    sql_dict = sql_parse(sql)
    where_list = []
    where_list.append(sql_dict.get("where"))
    with open("%s" % table_name, "r", encoding="utf_8") as fr,\
            open("%s" % table_bak, "w", encoding="utf-8")as fw:
        for line in fr:
            # 将文件中的数据读取切片配对，形成字典类型，然后利用函数logic_action()进行判断
            f_dict = dict(zip(tittle.split(","), line.strip().split(",")))
            logic = logic_action(where_list, f_dict)
            # 遍历[['dept', 'Market'], ['phone', '13566677787']]，当where条件为True时，
            # 将符合条件为True数据key 重新赋值
            for i in set_values:
                if logic:
                    key = i[0]
                    vla = i[1]
                    f_dict[key] = vla
                    count += 1
        # 将已经set更新完毕的全部数据，切片提取写入文件
            w_line = []
            for i in tittle.split(","):
                w_line.append(f_dict[i])

            w_line = ','.join(w_line)
            fw.write("%s\n" % w_line)
            fw.flush()
        # 文件需要关闭，才能进行重命名或者删除任务，不然会报错
        fr.close()
        os.remove("%s" % table_name)
        fw.close()
        os.rename("%s" % table_bak, "%s" % table_name)
        return print("更新成功，更新%d条数据中的%d个值" % (count-1, count))

def select(sql_dict):
    """
    此函数通过 where ,limit ,* ,like 等关键字条件筛选出符合条件的数据返回
    :param sql_dict : sql语句的字典类型
    :return  final_res 返回最终的查询结果
    """
    table_name = sql_dict["from"][0]
    with open("%s" % table_name, "r+", encoding='utf-8') as f:
            content_list = f.readlines()
            sql_dict["where"] = where_parse(sql_dict.get("where"))
            fifter_res = where_action(content_list, sql_dict["where"])
            limit_res = limit_parse(fifter_res, sql_dict["limit"])
            final_res = select_action(sql_dict["select"], limit_res)
    return final_res

def where_parse(where_list):
    """
    此函数是对sql语句中的where条件进行进一步处理
    :param where_list : 列表类型sql中的where条件['id', '>', '2', 'and', 'id', '<', '10']
    :return 返回 where_res [['id', '>', '2'], 'and', ['id', '<', '10']]
    """
    where_res = []
    key_k = ["not", "and", "or"]
    key_w = ''
    temp = []
    # 如果列表不为空，警报为False
    if where_list:
        tag = False
        for i in where_list:
            # 循环到key关键字and时，警报拉响，key_w赋值为and,where_res添加['id', '>', '2']进入列表
            # 再把temp列表清空，方便存储下一个id条件
            if i in key_k:
                tag = True
                key_w += i
                # 如果temp 不为空
                if temp:
                    where_res.append(temp)
                temp = []
            # 第一次temp 搜集的元素为['id', '>', '2'],第二次收集的元素为["<","10"]
            # 加上关闭警报时temp添加的i,第二次temp为['id', '<', '10']
            if not tag and i not in key_k:
                temp.append(i)
            # 满足此条件时说明 i循环到and 后面的 “id”，警报关闭 where_res 添加and 进入列表
            if tag and i not in key_k:
                tag = False
                where_res.append(key_w)
                key_w = ''
                # 此时temp列表中为["id"]
                temp.append(i)
        else:
            # where_res 再添加第二次的temp['id', '<', '10']
            where_res.append(temp)
    return where_res

def where_action(f, where_res):
    """
    :param f  = f.readlines()将所以数据读取出来 存放在列表中
    :param where_res 经过where_prase()进一步解析的where_res
    """
    tittle = "id,name,age,phone,dept,enroll_date"
    #  res_list用于存放结果集
    res_list = []
    # if len(where_list)!=0
    if where_res:
        for line in f:
            file_dict = dict(zip(tittle.split(","), line.strip().split(",")))
            logic_res = logic_action(where_res, file_dict)
            # 如果比对结果为True，将满足条件的line 添加进列表并返回
            if logic_res:
                res_list.append(line)
        return res_list
    else:
        # 说明没有where 条件为空 返回所有数据
        res_list = f
        return res_list


def logic_action(where_res, file_dict):
    """
    :param where_res 经过where_prase()进一步解析的where条件
    :param file_dict 字典类型数据库数据
    :return res 最后的比对结果，where条件跟与数据库每一条数据比对的结果
    """
    logic_res = []
    for item in where_res:
        if (type(item) == list):
            # ['id', '>', '1'] 多元赋值
            item_k, opt, item_v = item
            dict_v = file_dict[item_k]
            if opt == "=":
                opt = "%s=" % opt
            if item_v.isdigit():
                dict_v = int(dict_v)
                item_v = int(item_v)
                # 当where 中没有like 的时候 通过逻辑运算符“> < =”判断True,False
            if opt != 'like':
                # eval("1<3")能够判断为 Ture 和 Flase
                item = str(eval("%s%s%s" % (dict_v, opt, item_v)))
            else:
                # 当where 中有like 的时候 通过成员运算符“ in ”判断True,False
                if item_v in dict_v:
                    item = "True"
                else:
                    item = "False"
        logic_res.append(item)
        # 将列表转换成字符串，因为eval 只能传入字符串
    logic_str = ' '.join(logic_res)
    res = eval('%s' % logic_str)
    return res
def limit_parse(fifter_res, limit):
    """
    :param fifter_res 经过where_action()函数筛选满足where条件的结果列表
    :param limit 是sql 语句中的 limit 的值
    """
    # 如果limit有值,将fifter_res 结果切片返回， 没有值返回 原本的fifter_res
    if limit:
        limit_list = fifter_res[0:int(limit[0])]
        return limit_list
    else:
        return fifter_res

def select_action(select_v, limit_res):
    """
    :param select_v 是sql 语句中“*”或者指定字段如“age,id,name”
    :param limit_res 经过limit_prase() 解析后的满足条件文件数据结果
    :return final_result 返回最后过滤的数据结果
    """
    final_result = []
    title = "id,name,age,phone,dept,enroll_date"
    # 如果字段为“*”就返回全部上一层全部数据，不进行过滤
    # 或者根据指定字段过滤相关信息
    if select_v[0] == "*":
        return limit_res
    else:
        for i in limit_res:
            temp = []
            dic = dict(zip(title.split(","), i.split(",")))
            for j in select_v[0].split(","):
                temp.append(dic[j])
            final_result.append(temp)
    return final_result

if __name__ == '__main__':
    while True:
        sql_list = input(">").strip().split()
        if len(sql_list) == 0:
            continue
        elif sql_list == "exit":
            break
        else:
            print("\33[1;33m结果如下：\33[0m")
            sql_action(sql_list)
