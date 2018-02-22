import sys
import os
import json
import requests

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from data.export_url import ExportERL
from foo.public_class import Public
from data.request_dict import RequestData
from foo.log_print import LOG
from foo.database import ConnectDatabase
import random,string,time


class B2cExport(Public):

    """
    B2C接口测试类
    """
    def __init__(self):
        super(B2cExport, self).__init__()
        self.request = RequestData()
        self.url = ExportERL()
        self.log = LOG()
        # self.adult_dict = {'ageType': '0',
        #                      'cardType': 'PP',
        #                      'cardIssuePlace': 'CN',
        #                      'cardExpired': '20221111',
        #                      'nationality': 'CN'}
        #
        # self.child_dict = {'ageType': '1',
        #                      'cardType': 'PP',
        #                      'cardIssuePlace': 'CN',
        #                      'cardExpired': '20211001',
        #                      'nationality': 'CN'}



    def search(self, *args):
        """
        根据传入参数，向B2C搜索接口发起请求
        :param args: arg[0]区分代理/平台采购（"PP","PF"), args[1]B2C接口获取实时route数据的请求参数名称（"PP_AC_RT"),
        args[2]区分B2C境内境外接口（domestic：境内，overseas：境外） args[3]区分是直飞/中转航程（1是直飞，2是中转）
        args[4]是区分测试环境接口url
        :return:
        """
        request_data = self.request.get_request_data(args[0], args[1], args[3])
        self.log.log_info("%s - %s - B2C %s Export_search.log" % (args[1], args[3], args[2]), "B2CExport_log",
                          "b2c search export request:  %s" % request_data)
        if args[2] == "domestic":
            search_re = requests.post(url=self.url.get_environment_export_url(args[4], "b2c_domestic_url", "search"),
                                      json=request_data)
        else:
            search_re = requests.post(url=self.url.get_environment_export_url(args[4], "b2c_overseas_url", "search"),
                                      json=request_data)
        search_route = search_re.json()
        if self.msg in search_route and len(search_route[self.msg]) > 0:
            self.log.log_warning("%s - %s - B2C %s Export_search.log" % (args[1], args[3], args[2]), "B2CExport_log",
                                 "b2c search error:  %s" % search_route[self.msg])
        self.log.log_info("%s - %s - B2C %s Export_search.log" % (args[1], args[3], args[2]), "B2CExport_log",
                          "b2c search export response:  %s" % search_route)
        # print("搜索", search_route)
        return search_route

    def verify(self, search_route, *args):
        """
        根据传入参数，向B2C校验接口发起请求
        :param search_route: B2C搜索接口的返回数据
        :param args: args[0]区分是直飞/中转航程（1是直飞，2是中转） ,args[1]B2C接口获取实时route数据的请求参数名称（"PP_AC_RT"),
        args[2]区分B2C境内境外接口（domestic：境内，overseas：境外）,args[3]区分是哪个测试环境（a:deva）
        """
        flight_search_route = Public.add_b2b_flight_route(self, search_route, args[0])
        pop_search_route = Public.pop_status(self, flight_search_route, "status")
        self.log.log_info("%s - %s - B2C %s Export_verify.log" % (args[1], args[0], args[2]), "B2CExport_log",
                          "b2c verify export request:  %s" % pop_search_route)
        if args[2] == "domestic":
            verify_re = requests.post(url=self.url.get_environment_export_url(args[3], "b2c_domestic_url", "verify"),
                                      json=pop_search_route)
        else:
            verify_re = requests.post(url=self.url.get_environment_export_url(args[3], "b2c_overseas_url", "verify"),
                                      json=pop_search_route)
        verify_data = verify_re.json()
        if self.msg in verify_data and len(verify_data[self.msg]) > 0:
            self.log.log_warning("%s - %s - B2C %s Export_verify.log" % (args[1], args[0], args[2]), "B2CExport_log",
                                 "b2c verify export error:  %s" % verify_data[self.msg])
        self.log.log_info("%s - %s - B2C %s Export_verify.log" % (args[1], args[0], args[2]), "B2CExport_log",
                          "b2c verify export response:  %s" % verify_data)
        # print("校验", verify_re.json())
        return verify_data

    # def add_adult_chl_dict(self):
    #     """
    #     给传入的请求参数里添加一个成人乘客信息
    #     :param dic: 请求参数
    #     :return:添加了成人乘客信息的字典
    #     """
    #     #adult
    #     # passengers = list()
    #     first_name = "".join(random.sample(string.ascii_uppercase, 3))
    #     last_name = "".join(random.sample(string.ascii_uppercase, 3))
    #     card_num = "CN" + "".join(random.sample(string.digits, 6))
    #     gender = "".join(random.sample("MF", 1))
    #     name = first_name + "/" + last_name
    #     self.random_adult_birth_data()
    #     self.adult_dict["birthday"] = self.adult_birth_date
    #     self.adult_dict["name"] = name
    #     self.adult_dict["cardNum"] = card_num
    #     self.adult_dict["gender"] = gender
    #     # self.conf_data.get_conf_data("adult_dict").setdefault("birthday", self.adult_birth_date)
    #     # self.conf_data.get_conf_data("adult_dict").setdefault("name", name)
    #     # self.conf_data.get_conf_data("adult_dict").setdefault("cardNum", card_num)
    #     # self.conf_data.get_conf_data("adult_dict").setdefault("gender", gender)
    #     # adult = self.conf_data.get_conf_data("adult_dict")
    #     #dic.setdefault("passengers", passengers)
    #     # print("添加成人乘客", dic)
    #     #chil
    #     child_first_name = "".join(random.sample(string.ascii_uppercase, 3))
    #     child_last_name = "".join(random.sample(string.ascii_uppercase, 3))
    #     child_card_num = "CN" + "".join(random.sample(string.digits, 6))
    #     child_gender = "".join(random.sample("MF", 1))
    #     child_name = child_first_name + "/" + child_last_name
    #     self.random_child_birth_data()
    #     self.child_dict["birthday"] = self.child_birth_date
    #     self.child_dict["name"] = child_name
    #     self.child_dict["cardNum"] = child_card_num
    #     self.child_dict["gender"] = child_gender
    #     # self.conf_data.get_conf_data("child_dict").setdefault("birthday", self.child_birth_date)
    #     # self.conf_data.get_conf_data("child_dict").setdefault("name", name)
    #     # self.conf_data.get_conf_data("child_dict").setdefault("cardNum", card_num)
    #     # self.conf_data.get_conf_data("child_dict").setdefault("gender", gender)
    #     # child = self.conf_data.get_conf_data("child_dict")
    #     #print(adult_dict, child_dict)
    #     return self.adult_dict, self.child_dict

    def create_order(self, verify_data, *args):
        """
        根据传入参数，向B2C生单接口发起请求
        :param verify_data:b2c校验接口返回的数据
        :param args: args[0]B2C接口获取实时route数据的请求参数名称（"PP_AC_RT"), ,args[1]区分B2C境内境外接口（domestic：境内，overseas：境外）
        args[2]区分是直飞/中转航程（1是直飞，2是中转）, args[3]区分代理/平台采购（"PP","PF"), args[4]区分是哪个测试环境（a:deva）
        :return:
        """
        pop_status_data = Public.pop_status(self, verify_data, "status")
        # print(type(pop_status_data["route"]["price"]["childPrice"]))
        if type(pop_status_data["route"]["price"]["childPrice"]) == int or float:
            add_passengers_data = Public.add_adult_child_dict(self, pop_status_data)
        else:
            add_passengers_data = Public.add_adult_dict(self, pop_status_data)
        self.log.log_info("%s - %s - B2C %s Export_create_order.log" % (args[0], args[2], args[1]), "B2CExport_log",
                          "b2c create order export request:  %s" % pop_status_data)
        add_contact_data = Public.add_contact_dict(self, add_passengers_data)
        # adult, child = self.add_adult_chl_dict()
        # add_contact_data["passengers"].append(adult)
        # add_contact_data["passengers"].append(child)
        encryption_data = Public.encryption(self, args[3], json.dumps(add_contact_data))
        self.log.log_info("%s - %s - B2C %s Export_create_order.log" % (args[0], args[2], args[1]), "B2CExport_log",
                          "b2c create order export request encryption text:  %s" % encryption_data)
        if args[1] == "domestic":
            order_re = requests.post(url=self.url.get_environment_export_url(args[4], "b2c_domestic_url", "order"),
                                     data=encryption_data)
        else:
            order_re = requests.post(url=self.url.get_environment_export_url(args[4], "b2c_overseas_url", "order"), data=encryption_data)
        encryption_order = order_re.text
        order_data = Public.decryption(self, args[3], encryption_order)
        order_data = Public.pop_status(self, order_data, "status")
        order_data = Public.add_flight_type(self, verify_data, order_data)
        if self.msg in order_data and len(order_data[self.msg]) > 0:
            self.log.log_warning("%s - %s - B2C %s Export_create_order.log" % (args[0], args[2], args[1]),
                                 "B2CExport_log", "b2c create order export error:  %s" % order_data[self.msg])
        # # 连接数据库，查看数据订单状态跟接口订单状态是否吻合
        # database = ConnectDatabase()
        # order_status = database.sql_order_status_query(order_data["orderNo"])
        # assert order_status == 1
        # self.log.log_info("%s - %s - B2C %s Export_create_order.log" % (args[0], args[2], args[1]), "B2CExport_log",
        #                   " create order success,orderNO:  %s, "
        #                   "corresponding database status:  %s" % (order_data["orderNo"], order_status))
        self.log.log_info("%s - %s - B2C %s Export_create_order.log" % (args[0], args[2], args[1]), "B2CExport_log",
                          "b2c create order export response:  %s" % order_data)
        # print("生单", order_data)
        return order_data

    def pay_verify(self, order_data, *args):
        """
        根据传入参数，向B2C支付前校验接口发起请求
        :param order_data:b2c生单接口返回的数据
        :param args: args[0]B2C接口获取实时route数据的请求参数名称（"PP_AC_RT"), ,args[1]区分B2C境内境外接口（domestic：境内，overseas：境外）
        args[2]区分是直飞/中转航程（1是直飞，2是中转）, args[3]区分代理/平台采购（"PP","PF"), args[4]区分是哪个测试环境（a:deva）
        :return:
        """
        self.log.log_info("%s - %s - B2C %s Export_pay_verify.log" % (args[0], args[2], args[1]), "B2CExport_log",
                          "b2c pay verify export request:  %s" % order_data)
        order_data = Public.encryption(self, args[3], json.dumps(order_data))
        self.log.log_info("%s - %s - B2C %s Export_pay_verify.log" % (args[0], args[2], args[1]), "B2CExport_log",
                          "b2c pay verify export request encryption text:  %s" % order_data)
        if args[1] == "domestic":
            pay_verify_re = requests.post(url=self.url.get_environment_export_url(args[4], "b2c_domestic_url", "pay_verify"),
                                          data=order_data)
        else:
            pay_verify_re = requests.post(url=self.url.get_environment_export_url(args[4], "b2c_overseas_url", "pay_verify"),
                                          data=order_data)
        encryption_pay_verify = pay_verify_re.text
        pay_verify_data = Public.decryption(self, args[3], encryption_pay_verify)
        if self.msg in pay_verify_data and len(pay_verify_data[self.msg]) > 0:
            self.log.log_warning("%s - %s - B2C %s Export_pay_verify.log" % (args[0], args[2], args[1]), "B2CExport_log",
                                 "b2c pay verify export error:  %s" % pay_verify_data[self.msg])
        self.log.log_info("%s - %s - B2C %s Export_pay_verify.log" % (args[0], args[2], args[1]), "B2CExport_log",
                          "b2c pay verify export response:  %s" % pay_verify_data)
        # print("支付前校验", pay_verify_data)
        return pay_verify_data

    def apply_ticketing(self, verify_data, pay_verify_data, *args):
        """
        根据传入参数，向B2C申请出票接口发起请求
        :param verify_data:b2c校验接口返回的数据
        :param pay_verify_data:支付前校验接口返回的数据
        :param args: args[0]B2C接口获取实时route数据的请求参数名称（"PP_AC_RT"), ,args[1]区分B2C境内境外接口（domestic：境内，overseas：境外）
        args[2]区分是直飞/中转航程（1是直飞，2是中转）, args[3]区分代理/平台采购（"PP","PF"), args[4]区分是哪个测试环境（a:deva),
        arg[5]区分是B2B类型接口还是B2C类型接口
        :return:
        """
        apply_ticketing_data = Public.compose_apply_ticketing_data(self, args[3], verify_data, pay_verify_data,
                                                                   args[5])
        self.log.log_info("%s - %s - B2C %s Export_apply_ticketing.log" % (args[0], args[2], args[1]), "B2CExport_log",
                          "b2c apply ticketing export request:  %s" % apply_ticketing_data)
        if args[1] == "domestic":
            apply_ticketing_re = requests.post(url=self.url.get_environment_export_url(args[4], "apply_ticketing_url", "domestic"),
                                               json=apply_ticketing_data)
        else:
            apply_ticketing_re = requests.post(url=self.url.get_environment_export_url(args[4], "apply_ticketing_url", "overseas"),
                                               json=apply_ticketing_data)
        apply_ticketing_data = apply_ticketing_re.json()
        if self.msg in apply_ticketing_data and "%s" % apply_ticketing_data[self.msg] != "None":
            self.log.log_warning("%s - %s - B2C %s Export_apply_ticketing.log" % (args[0], args[2], args[1]),
                                 "B2CExport_log", "b2c apply ticketing export error:  %s" % apply_ticketing_data[self.msg])
        # # 连接数据库，查看数据订单状态跟接口订单状态是否吻合
        # database = ConnectDatabase()
        # order_status = database.sql_order_status_query(apply_ticketing_data["orderNo"])
        # assert order_status == 9
        # self.log.log_info("%s - %s - B2C %s Export_apply_ticketing.log" % (args[0], args[2], args[1]), "B2CExport_log",
        #                   " apply ticketing success,orderNO:  %s, "
        #                   "corresponding database status:  %s" % (apply_ticketing_data["orderNo"], order_status))
        self.log.log_info("%s - %s - B2C %s Export_apply_ticketing.log" % (args[0], args[2], args[1]), "B2CExport_log",
                          "b2c export flight apply ticketing response:  %s" % apply_ticketing_data)
        # print("申请出票", apply_ticketing_re.text)

    def order_query(self, verify_data, pay_verify_data, *args):
        """
        根据传入参数，向订单查询接口发起请求
        :param verify_data:b2c校验接口返回的数据
        :param pay_verify_data:支付前校验接口返回的数据
        :param args: args[0]B2C接口获取实时route数据的请求参数名称（"PP_AC_RT"), ,args[1]区分B2C境内境外接口（domestic：境内，overseas：境外）
        args[2]区分是直飞/中转航程（1是直飞，2是中转）, args[3]区分代理/平台采购（"PP","PF"), args[4]区分是哪个测试环境（a:deva)
        :return:
        """
        order_query_data = Public.compose_order_query_data(self, args[3], verify_data, pay_verify_data)
        self.log.log_info("%s - %s - B2C %s Export_order_query.log" % (args[0], args[2], args[1]), "B2CExport_log",
                          "b2c order query export request:  %s" % order_query_data)
        if args[1] == "domestic":
            order_query_re = requests.post(url=self.url.get_environment_export_url(args[4], "order_query_url", "domestic"),
                                           json=order_query_data)
        else:
            order_query_re = requests.post(url=self.url.get_environment_export_url(args[4], "order_query_url", "overseas"),
                                           json=order_query_data)
        order_query_json = order_query_re.json()
        self.log.log_info("%s - %s - B2C %s Export_order_query.log" % (args[0], args[2], args[1]), "B2CExport_log",
                          "b2c order query export response:  %s" % order_query_json)
        # print("订单查询", order_query_re.text)

    def b2c_export_logic(self, *args):
        """
        B2C运价直连接口逻辑主流程
        :param args: args[0]区分代理/平台采购（"PP","PF"), arg[1]B2C接口获取实时route数据的请求参数名称（"PP_AC_RT"),
        args[2]区分B2C境内境外接口（domestic：境内，overseas：境外）, args[3]区分b2b或者b2c接口, args[4]区分是直飞/中转航程（1是直飞，2是中转）,
        args[5]区分是哪个测试环境（a:deva)
        """
        # try:
        search_route = self.search(args[0], args[1], args[2], args[4], args[5])
        verify_data = self.verify(search_route, args[4], args[1], args[2], args[5])
        order_data = self.create_order(verify_data, args[1], args[2], args[4], args[0], args[5])
        pay_verify_data = self.pay_verify(order_data, args[1], args[2], args[4], args[0], args[5])
        self.apply_ticketing(verify_data, pay_verify_data, args[1], args[2], args[4], args[0], args[5], args[3])
        #self.order_query(verify_data, pay_verify_data, args[1], args[2], args[4], args[0], args[5])
        time.sleep(1)
        # except Exception as e:
        #     print(e)


if __name__ == "__main__":
    start = B2cExport()
    start.b2c_export_logic("PP", "PP_A_OW", "domestic", "b2c", 1, "a")