import random
import string
import time
import sys
import os
import requests

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from data.conf_dict import ConfData
from data.export_url import ExportERL
from data.request_dict import RequestData


class Public(object):

    """
    公共函数类，提供其他逻辑类使用的公用函数
    """
    def __init__(self):
        self.len_args = 0
        self.adult_birth_date = ""
        self.child_birth_date = ""
        self.msg = "msg"
        # self.passengers = list()
        self.b2c_direct_flight_list = list()
        self.b2b_direct_flight_list = list()
        self.b2c_transfer_flight_list = list()
        self.b2b_transfer_flight_list = list()
        self.filter_share_combined_transport_list = list()   # 用于保存已过滤共享和联运的航程信息
        self.fromSegments = list()
        self.order_query_dict = dict()
        self.apply_ticketing_dict = dict()
        self.headers = {"Content-Type": "application/data;charset=utf-8"}
        self.flightType = "flightType"
        self.url = ExportERL()
        self.conf_data = ConfData()
        self.request_data = RequestData()

    def encryption(self, purchase_type, data):
        """
        数据加密
        :param data:待加密数据
        :return:加密数据
        """
        if purchase_type == "PP":
            self.headers.setdefault("Key", self.conf_data.get_conf_data("pp_key"))
        else:
            self.headers.setdefault("Key", self.conf_data.get_conf_data("pf_key"))
        encryption = requests.post(url=self.url.get_export_url("encryption_url", "url"), headers=self.headers, data=data)
        encryption_text = encryption.text
        # print("加密", encryption_text)
        return encryption_text

    def decryption(self, purchase_type, data):
        """
        数据解密
        :param data:待解密数据
        :return:解密数据
        """
        if purchase_type == "PP":
            self.headers.setdefault("Key", self.conf_data.get_conf_data("pp_key"))
        else:
            self.headers.setdefault("Key", self.conf_data.get_conf_data("pf_key"))
        decryption = requests.post(url=self.url.get_export_url("decryption_url", "url"), headers=self.headers, data=data)
        decryption_text = decryption.json()
        # print("解密", decryption_text)
        return decryption_text


    def add_adult_dict(self, dic):
        """
        给传入的请求参数里添加一个成人乘客信息
        :param dic: 请求参数
        :return:添加了成人乘客信息的字典
        """
        passengers = list()
        first_name = "".join(random.sample(string.ascii_uppercase, 3))
        last_name = "".join(random.sample(string.ascii_uppercase, 3))
        card_num = "CN" + "".join(random.sample(string.digits, 5))
        gender = "".join(random.sample("MF", 1))
        name = first_name + "/" + last_name
        self.random_adult_birth_data()
        self.conf_data.get_conf_data("adult_dict").setdefault("birthday", self.adult_birth_date)
        self.conf_data.get_conf_data("adult_dict").setdefault("name", name)
        self.conf_data.get_conf_data("adult_dict").setdefault("cardNum", card_num)
        self.conf_data.get_conf_data("adult_dict").setdefault("gender", gender)
        passengers.append(self.conf_data.get_conf_data("adult_dict"))
        dic.setdefault("passengers", passengers)
        # print("添加成人乘客", dic)
        return dic

    def add_adult_child_dict(self, dic):
        """
        给传入的请求参数添加一个成人乘客信息和一个儿童乘客信息
        :param dic: 请求参数
        :return:添加了乘客信息请求参数
        """
        first_name = "".join(random.sample(string.ascii_uppercase, 3))
        last_name = "".join(random.sample(string.ascii_uppercase, 3))
        card_num = "CN" + "".join(random.sample(string.digits, 5))
        gender = "".join(random.sample("MF", 1))
        name = first_name + "/" + last_name
        self.random_child_birth_data()
        self.conf_data.get_conf_data("child_dict").setdefault("birthday", self.child_birth_date)
        self.conf_data.get_conf_data("child_dict").setdefault("name", name)
        self.conf_data.get_conf_data("child_dict").setdefault("cardNum", card_num)
        self.conf_data.get_conf_data("child_dict").setdefault("gender", gender)
        passengers_dic = self.add_adult_dict(dic)
        passengers_dic["passengers"].append(self.conf_data.get_conf_data("child_dict"))
        # print("添加儿童乘客", passengers_dic)
        return passengers_dic

    def add_contact_dict(self, dic):
        """
        给传入的请求参数添加联系人信息
        :param dic:请求参数
        :return:添加联系人信息后的请求参数
        """
        first_name = "".join(random.sample(string.ascii_uppercase, 3))
        last_name = "".join(random.sample(string.ascii_uppercase, 3))
        address = "".join(random.sample(string.ascii_uppercase, 6))
        mobile = "185" + "".join(random.sample(string.digits, 8))
        name = first_name + "/" + last_name
        self.conf_data.get_conf_data("contact_dict").setdefault("name", name)
        self.conf_data.get_conf_data("contact_dict").setdefault("address", address)
        self.conf_data.get_conf_data("contact_dict").setdefault("mobile", mobile)
        dic.setdefault("contact", self.conf_data.get_conf_data("contact_dict"))
        # print("添加联系人", dic)
        return dic

    def pop_status(self, dic, *args):
        """
        给传入的请求参数删除多余字段,添加缺少字段
        :param dic: 请求参数
        :return:删除后的请求参数
        """
        self.len_args = len(args)
        for i in range(self.len_args):
            dic.pop(args[i])

        return dic

    def add_flight_type(self, verify_dic, pay_verify_dic):
        """
         从校验接口返回的json数据中提取信息，给支付前校验接口请求参数添加缺少字段
        :param verify_dic: 校验接口返回的数据
        :param pay_verify_dic: 支付前校验接口请求参数
        :return:添加后的请求参数
        """
        pay_verify_dic.setdefault(self.flightType, verify_dic[self.flightType])
        return pay_verify_dic

    def compose_apply_ticketing_data(self, purchase_type, data, dic, *args):
        """
        从支付前校验接口返回的json数据中提取信息，拼接成申请出票的请求参数
        :param purchase_type: 代理/平台采购（"PP","PF"）
        :param data:校验接口返回参数
        :param dic:支付前校验接口返回参数
        :param args:args[0]区分b2b或者B2C接口
        :return:
        """
        # print(purchase_type, data, dic)
        order_no = dic["orderNo"]
        if args[0] == "b2c":
            if type(dic["route"]["price"]["childPrice"]) == int or float:
                order_price = (dic["route"]["price"]["adultPrice"] + dic["route"]["price"]["adultTax"] +
                               dic["route"]["price"]["childPrice"] + dic["route"]["price"]["childTax"]) + 200
                print("hello")
            else:
                order_price = dic["route"]["price"]["adultPrice"] + dic["route"]["price"]["adultTax"]
        else:
            if type(dic["routing"]["childPrice"]) == int:
                order_price = (dic["routing"]["adultPrice"] + dic["routing"]["adultTax"] +
                               dic["routing"]["childPrice"] + dic["routing"]["childTax"]) + 200
            else:
                order_price = dic["routing"]["adultPrice"] + dic["routing"]["adultTax"] + 200
        # print("order_price", order_price)
        print(order_price)
        if purchase_type == "PP":
            token = "%s#%s#%s" % (str(order_price), order_no, self.conf_data.get_conf_data("pp_key"))
        else:
            token = "%s#%s#%s" % (str(order_price), order_no, self.conf_data.get_conf_data("pf_key"))
        self.apply_ticketing_dict["token"] = self.encryption(purchase_type, token)
        self.apply_ticketing_dict["cid"] = data["cid"]
        # print("申请出票参数", self.apply_ticketing_dict)

        return self.apply_ticketing_dict

    def compose_order_query_data(self, purchase_type, data, dic):
        """
        从支付前校验接口返回的json数据中提取信息，拼接成订单查询的请求参数
        :param purchase_type: 代理/平台采购（"PP","PF"）
        :param data: 校验接口返回参数
        :param dic: 支付前校验接口返回参数
        :return:
        """

        order_no = dic["orderNo"]
        if purchase_type == "PP":
            token = "%s#%s" % (order_no, self.conf_data.get_conf_data("pp_key"))
        else:
            token = "%s#%s" % (order_no, self.conf_data.get_conf_data("pf_key"))
        self.order_query_dict["token"] = self.encryption(purchase_type, token)
        self.order_query_dict["cid"] = data["cid"]
        # print("订单查询参数", self.order_query_dict)
        return self.order_query_dict

    def add_direct_flight(self, search_route):
        """
        从B2C search接口返回的json数据中，选择直飞航班拼接至校验接口的请求参数
        :param search_route:B2C search接口返回的json数据，也是后续校验接口的请求参数
        :return:
        """
        for i in search_route["route"]:
            if len(i["fromSegments"]) == 1:
                self.b2c_direct_flight_list.append(i)
        # print("中转航班列表", self.b2c_direct_flight_list)
        search_route["route"] = random.sample(self.b2c_direct_flight_list, 1)[0]
        # print("search_route", search_route)
        return search_route

    def add_transfer_flight(self, search_route):
        """
        从B2C search接口返回的json数据中，选择中转航班拼接至校验接口的请求参数
        :param search_route:B2C search接口返回的json数据，也是后续校验接口的请求参数
        :return:
        """
        for i in search_route["route"]:
            if len(i["fromSegments"]) == 2:
                self.b2c_transfer_flight_list.append(i)
        # print("中转航班列表", self.b2c_transfer_flight_list)
        search_route["route"] = random.sample(self.b2c_transfer_flight_list, 1)[0]
        # print("search_route", search_route)
        return search_route

    def add_b2b_flight_route(self, search_route, flag):
        """
        从B2C search接口返回的json数据中，根据传入参数flag拼接B2C校验接口的请求参数
        :param search_route: B2C search接口返回的json数据，也是后续校验接口的请求参数
        :param flag: 1代表直飞航班标志，2代表中转直飞标志
        :return:
        """
        print(search_route)
        if flag == 1:
            for i in search_route["route"]:
                if len(i["fromSegments"]) == 1:
                    self.b2c_direct_flight_list.append(i)
            # print("直飞航班列表", self.b2c_direct_flight_list)
            search_route["route"] = random.sample(self.b2c_direct_flight_list, 1)[0]
            # print("search_route", search_route)
            return search_route
        else:
            for i in search_route["route"]:
                if len(i["fromSegments"]) == 2:
                    self.b2c_transfer_flight_list.append(i)
            # print("中转航班列表", self.b2c_transfer_flight_list)
            print(self.b2c_transfer_flight_list)
            search_route["route"] = random.sample(self.b2c_transfer_flight_list, 1)[0]
            # print("search_route", search_route)
            return search_route

    # def add_flight_routing(self, search_route, *args):
    #     """
    #     从B2C search接口返回的json数据中，选择航班拼接成为B2B search接口的请求参数
    #     :param search_route:B2C search接口返回的json数据，也是后续校验接口的请求参数
    #     :param args: 第一个位置参数是区分走b2c/b2b逻辑，第二个位置参数是区别平台/代理采购，
    #             第三个位置参数是区别拼接直飞/中转航班, 第四个位置参数是区分单程/往返航程，如果是往返航程，就在RetSegments字段中添加返程信息
    #     :return:
    #     """
    #     if args[2] == 1:
    #         for i in search_route["route"]:
    #             if len(i["fromSegments"]) == 1:
    #                 self.b2c_direct_flight_list.append(i)
    #                 # 过滤B2B直飞共享航班
    #                 if i["fromSegments"][0]["codeShare"] == 1:
    #                     continue
    #                 else:
    #                     self.b2b_direct_flight_list.append(i["fromSegments"])
    #         # print("b2b直飞航班列表", self.b2b_direct_flight_list)
    #         # print("b2c直飞航班列表", self.b2c_direct_flight_list)
    #         if args[0] == "b2b" and args[1] == "PP":
    #             b2b_request = self.request_data.get_b2b_request_data("PP")
    #             b2b_request["routing"]["fromSegments"] = random.sample(self.b2b_direct_flight_list, 1)[0]
    #             return b2b_request
    #         elif args[0] == "b2b" and args[1] == "PF":
    #             b2b_request = self.request_data.get_b2b_request_data("PF")
    #             b2b_request["routing"]["fromSegments"] = random.sample(self.b2b_direct_flight_list, 1)[0]
    #             return b2b_request
    #         else:
    #             search_route["route"] = random.sample(self.b2c_direct_flight_list, 1)[0]
    #             return search_route
    #     else:
    #         for i in search_route["route"]:
    #             if len(i["fromSegments"]) == 2:
    #                 self.b2c_transfer_flight_list.append(i)
    #                 self.b2b_transfer_flight_list.append(i["fromSegments"])
    #         b2b_transfer_flight_list = self.filter_share_combined_transport()
    #         # print("b2b中转航班列表", b2b_transfer_flight_list)
    #         # print("b2c中转航班列表", self.b2c_transfer_flight_list)
    #         if args[0] == "b2b" and args[1] == "PP":
    #             b2b_request = self.request_data.get_b2b_request_data("PP")
    #             b2b_request["routing"]["fromSegments"] = random.sample(b2b_transfer_flight_list, 1)[0]
    #             return b2b_request
    #         elif args[0] == "b2b" and args[1] == "PF":
    #             b2b_request = self.request_data.get_b2b_request_data("PF")
    #             b2b_request["routing"]["fromSegments"] = random.sample(b2b_transfer_flight_list, 1)[0]
    #             return b2b_request
    #         else:
    #             search_route["route"] = random.sample(self.b2c_transfer_flight_list, 1)[0]
    #         return search_route

    def filter_share_combined_transport(self, flight_list):
        """
        过滤共享和联运航程
        :return:已过滤共享和联运的航程列表
        """
        airline_company_list = list()  # 用于保存航程信息中的航司信息
        code_share_list = list()  # 用于保存codeShare字段中的内容

        i_list = list()   # 保存每个航程fromSegments 和 retSegments 中的元素
        # for i in dic["route"]:
        #     self.fromSegments.append(i)
        for i in flight_list:
            for j in range(len(i["fromSegments"])):
                i_list.append(i["fromSegments"][j])
            for k in range(len(i["retSegments"])):
                i_list.append(i["retSegments"][k])
            for j in range(len(i_list)):
                code_share_list.append(i_list[j]["codeShare"])
                airline_company_list.append(i_list[j]["flightNumber"][:2])
            if len(airline_company_list) == len(i_list):
                code_share_list = list(set(code_share_list))
                airline_company_list = list(set(airline_company_list))
                if len(airline_company_list) == 1 and True not in code_share_list:
                    self.filter_share_combined_transport_list.append(i)
                    # print("True")
                    airline_company_list = []
                    code_share_list = []
                    i_list = []
                else:
                    # print("FALSE")
                    airline_company_list = []
                    code_share_list = []
                    i_list = []

        return self.filter_share_combined_transport_list

    def random_adult_birth_data(self):
        """
        随机产生成人生日
        :return:null
        """
        start_date = (1980, 1, 1, 0, 0, 0, 0, 0, 0)       # 设置开始日期时间元组（1980-01-01 00：00：00）
        end_date = (1995, 12, 31, 23, 59, 59, 0, 0, 0)    # 设置结束日期时间元组（1995-12-31 23：59：59）
        start = time.mktime(start_date)    # 生成开始时间戳
        end = time.mktime(end_date)      # 生成结束时间戳
        # 随机生成10个日期字符串
        for i in range(10):
            t = random.randint(start, end)    # 在开始和结束时间戳中随机取出一个
            date_tuple = time.localtime(t)          # 将时间戳生成时间元组
            date = time.strftime("%Y-%m-%d", date_tuple)  # 将时间元组转成格式化字符串（1976-05-21）
            self.adult_birth_date = date

    def random_child_birth_data(self):
        """
        随机产生儿童生日
        :return:null
        """
        start_date = (2012, 1, 1, 0, 0, 0, 0, 0, 0)       # 设置开始日期时间元组
        end_date = (2015, 8, 8, 8, 8, 8, 0, 0, 0)    # 设置结束日期时间元组
        start = time.mktime(start_date)    # 生成开始时间戳
        end = time.mktime(end_date)      # 生成结束时间戳
        # 随机生成10个日期字符串
        for i in range(10):
            t = random.randint(start, end)    # 在开始和结束时间戳中随机取出一个
            date_tuple = time.localtime(t)          # 将时间戳生成时间元组
            date = time.strftime("%Y-%m-%d", date_tuple)  # 将时间元组转成格式化字符串（1976-05-21）
            self.child_birth_date = date

    def add_flight_rout(self, search_route, *args):
        """
        从B2C search接口返回的json数据中，选择航班拼接成为B2B search接口的请求参数
        :param search_route:B2C search接口返回的json数据，也是后续校验接口的请求参数
        :param args: 第一个位置参数是区分走b2c/b2b逻辑，第二个位置参数是区别平台/代理采购，
                第三个位置参数是区别拼接直飞/中转航班, 第四个位置参数是区分单程/往返航程，如果是往返航程，就在RetSegments字段中添加返程信息
        :return:
        """
        if args[2] == 1:
            for i in search_route["route"]:
                if len(i["fromSegments"]) == 1:
                    self.b2c_direct_flight_list.append(i)
                    self.b2b_direct_flight_list.append(i)  # ["fromSegments"]
            b2b_direct_flight_list = self.filter_share_combined_transport(self.b2b_direct_flight_list)
            # print("b2b直飞航班列表", b2b_direct_flight_list)
            # print("b2c直飞航班列表", self.b2c_direct_flight_list)
            if args[0] == "b2b" and args[1] == "PP":
                b2b_request = self.request_data.get_b2b_request_data("PP")
                b2b_request["routing"] = random.sample(b2b_direct_flight_list, 1)[0]
                return b2b_request
            elif args[0] == "b2b" and args[1] == "PF":
                b2b_request = self.request_data.get_b2b_request_data("PF")
                b2b_request["routing"] = random.sample(b2b_direct_flight_list, 1)[0]
                return b2b_request
            else:
                search_route["route"] = random.sample(self.b2c_direct_flight_list, 1)[0]
                return search_route
        else:
            for i in search_route["route"]:
                if len(i["fromSegments"]) == 2:
                    self.b2c_transfer_flight_list.append(i)
                    self.b2b_transfer_flight_list.append(i)
            b2b_transfer_flight_list = self.filter_share_combined_transport(self.b2b_transfer_flight_list)
            # print("b2b中转航班列表", b2b_transfer_flight_list)
            # print("b2c中转航班列表", self.b2c_transfer_flight_list)
            if args[0] == "b2b" and args[1] == "PP":
                b2b_request = self.request_data.get_b2b_request_data("PP")
                b2b_request["routing"] = random.sample(b2b_transfer_flight_list, 1)[0]
                return b2b_request
            elif args[0] == "b2b" and args[1] == "PF":
                b2b_request = self.request_data.get_b2b_request_data("PF")
                b2b_request["routing"] = random.sample(b2b_transfer_flight_list, 1)[0]
                return b2b_request
            else:
                search_route["route"] = random.sample(self.b2c_transfer_flight_list, 1)[0]
            return search_route

if __name__ == "__main__":
    p = Public()
    # a,b = p.add_adult_chl_dict()
    # print(a,b)
    # p.add_flight_rout(data, "b2b", "PP", 2)
    # p.filter_share_combined_transport()