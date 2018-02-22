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


class B2BExport(Public):

    """
    B2B接口测试类
    """

    def __init__(self):
        super(B2BExport, self).__init__()
        self.request = RequestData()
        self.url = ExportERL()
        self.log = LOG()
        self.msg = "msg"

    def search(self, *args):
        """
        从B2C搜索接口(境内)，获取实时route数据，然后拼接到b2b的请求参数中进行搜索
        :param args arg[0]区分代理/平台采购（"PP","PF"）， arg[1]B2C接口获取实时route数据的请求参数名称（"PP_AC_RT"）
         arg[2] 区分B2B/B2C接口("b2b"/"b2c")， arg[3]区分是直飞/中转航程（1是直飞，2是中转）,args[4]测试环境地址
        :return:
        """
        request_data = self.request.get_request_data(args[0], args[1], args[3])
        search_re = requests.post(url=self.url.get_environment_export_url(args[4], "b2c_domestic_url", "search"),
                                  json=request_data)
        search_route = search_re.json()
        if self.msg in search_route and len(search_route[self.msg]) > 0:
            self.log.log_warning("B2CExport_search.log", "B2BExport_log", "b2b search error:  " + search_route[self.msg])
        search_route = Public.add_flight_rout(self, search_route, args[2], args[0], args[3])
        search_route["childrenNum"] = request_data["childrenNum"]
        # print("B2B请求参数", search_route)
        self.log.log_info("%s - %s - B2B Export_search.log" % (args[1], args[3]), "B2BExport_log",
                          "b2b search export request:  %s" % search_route)
        search_re = requests.post(url=self.url.get_environment_export_url(args[4], "b2b_export_url", "search"),
                                  json=search_route)
        search_route = search_re.json()
        if self.msg in search_route and len(search_route[self.msg]) > 0:
            self.log.log_warning("%s - %s - B2B Export_search.log" % (args[1], args[3]), "B2BExport_log",
                                 "b2b search error:  %s" % search_route[self.msg])

        self.log.log_info("%s - %s - B2B Export_search.log" % (args[1], args[3]), "B2BExport_log",
                          "b2b search export response:  %s" % search_route)
        return search_route, request_data

    def create_order(self, search_route, request_data, *args):
        """
        根据传入参数,向B2B生单接口发起生单请求进行圣单
        :param search_route:B2B生单接口的请求参数
        :param request_data:B2C搜索接口的请求参数
        :param args[0]B2C接口获取实时route数据的请求参数名称（"PP_AC_RT"）, args[1]区分是直飞/中转航程（1是直飞，2是中转）args[2]测试环境地址
        :return:
        """

        if search_route["routing"]["childPrice"] > 0:
            add_passengers = Public.add_adult_child_dict(self, search_route)
        else:
            add_passengers = Public.add_adult_dict(self, search_route)
        add_contact = Public.add_contact_dict(self, add_passengers)
        add_contact = Public.pop_status(self, add_contact, "status", "msg", "maxSeats", "rule")
        add_contact.setdefault("cid", request_data["cid"])
        add_contact.setdefault("tripType", request_data["flightType"])
        encryption_text = Public.encryption(self, "PP", json.dumps(add_contact))
        self.log.log_info("%s - %s - B2B Export_create_order.log" % (args[0], args[1]), "B2BExport_log",
                          "b2b create order request:  %s" % add_contact)
        self.log.log_info("%s - %s - B2B Export_create_order.log" % (args[0], args[1]), "B2BExport_log",
                          "b2b create order request encryption text:  %s" % encryption_text)
        search_re = requests.post(url=self.url.get_environment_export_url(args[2], "b2b_export_url", "order"),
                                  json=encryption_text)
        decryption_text = Public.decryption(self, "PP", search_re.text)
        self.log.log_info("%s - %s - B2B Export_create_order.log" % (args[0], args[1]), "B2BExport_log",
                          "b2b create order export response:  %s" %
                          decryption_text)
        # print("order", decryption_text)
        if self.msg in decryption_text and len(decryption_text[self.msg]) > 0:
            self.log.log_warning("%s - %s - B2B Export_create_order.log" % (args[0], args[1]), "B2BExport_log",
                                 "b2b create order error:  %s" %
                                 decryption_text[self.msg])
        # 连接数据库，查看数据订单状态跟接口订单状态是否吻合
        database = ConnectDatabase()
        order_status = database.sql_order_status_query(decryption_text["orderNo"])
        assert order_status == 1
        self.log.log_info("%s - %s - B2B Export_create_order.log" % (args[0], args[1]), "B2BExport_log",
                          " create order success,orderNO:  %s"
                          "corresponding database status:  %s" % (decryption_text["orderNo"], order_status))
        return decryption_text

    def pay_verify(self, order_data, request_data, *args):
        """
        B2B支付前校验接口，根据传入参数发起支付前校验请求，进行支付前检验
       :param order_data:支付前校验接口的请求参数
       :param request_data:B2C搜索接口的请求参数
       :param args[0]B2C接口获取实时route数据的请求参数名称（"PP_AC_RT"）, args[1]区分是直飞/中转航程（1是直飞，2是中转）
       args[2]测试环境地址
       :return:
       """
        order_data = Public.pop_status(self, order_data, "status")
        order_data.setdefault("cid", request_data["cid"])
        order_data.setdefault("tripType", request_data["flightType"])
        self.log.log_info("%s - %s - B2B Export_pay_verify.log" % (args[0], args[1]), "B2BExport_log",
                          "b2b pay_verify export request:  %s" % order_data)
        order_after_data = Public.encryption(self, "PP", json.dumps(order_data))
        self.log.log_info("%s - %s - B2B Export_pay_verify.log" % (args[0], args[1]), "B2BExport_log",
                          "b2b pay_verify export request encryption text:  %s" % order_after_data)
        pay_verify_re = requests.post(url=self.url.get_environment_export_url(args[2], "b2b_export_url", "pay_verify"),
                                      data=order_after_data)
        pay_verify_data = Public.decryption(self, "PP", pay_verify_re.text)
        # print("pay_verify_data", pay_verify_data)
        if self.msg in pay_verify_data and len(pay_verify_data[self.msg]) > 0:
            self.log.log_info("%s - %s - B2B Export_pay_verify.log" % (args[0], args[1]), "B2BExport_log",
                              "b2b pay_verify export error:  %s" % pay_verify_data[self.msg])
        self.log.log_info("%s - %s - B2B Export_pay_verify.log" % (args[0], args[1]), "B2BExport_log",
                          "b2b pay_verify export response:  %s" % pay_verify_data)
        return pay_verify_data

    def apply_ticketing(self, purchase_type, data, pay_verify_data, flag, *args):
        """
        根据传入参数向B2B申请出票接口发起申请出票请求，进行申请出票
        :param purchase_type: 采购商类型 “PP”“PF”
        :param data: B2C搜索接口的请求参数
        :param pay_verify_data: 支付前校验接口的返回的参数
        :param flag: 境内境外标识
        :param args: agr[0] 区分B2B或者B2C接口  args[1]B2C接口获取实时route数据的请求参数名称（"PP_AC_RT"）
        args[2]区分是直飞/中转航程（1是直飞，2是中转）,args[3]测试环境地址
        :return:
        """
        apply_ticketing_data = Public.compose_apply_ticketing_data(self, purchase_type, data, pay_verify_data, args[0])
        self.log.log_info("%s - %s - B2B Export_apply_ticketing.log" % (args[1], args[2]), "B2BExport_log",
                          "b2b apply_ticketing export request:  %s" % apply_ticketing_data)
        if flag == "domestic":
            apply_ticketing_re = requests.post(url=self.url.get_environment_export_url(args[3], "apply_ticketing_url", "domestic"),
                                               json=apply_ticketing_data)
        else:
            apply_ticketing_re = requests.post(url=self.url.get_environment_export_url(args[3], "apply_ticketing_url", "overseas"),
                                               json=apply_ticketing_data)
        apply_ticketing_data = apply_ticketing_re.json()
        # 连接数据库，查看数据订单状态跟接口订单状态是否吻合
        database = ConnectDatabase()
        order_status = database.sql_order_status_query(apply_ticketing_data["orderNo"])
        assert order_status == 9

        self.log.log_info("%s - %s - B2B Export_apply_ticketing.log" % (args[1], args[2]), "B2BExport_log",
                          "b2b apply_ticketing export response:  %s" % apply_ticketing_data)
        # print("申请出票", apply_ticketing_data)

    def order_query(self, purchase_type, data, pay_verify_data, flag, *args):
        """
        根据传入参数向B2B订单查询接口发起查询请求，进行订单查询
        :param purchase_type: 采购商类型 “PP”“PF”
        :param data: B2C搜索接口的请求参数
        :param pay_verify_data: 支付前校验接口的返回的参数
        :param flag: 境内境外标识
        :param args: agr[0] B2C接口获取实时route数据的请求参数名称（"PP_AC_RT"）  args[1]区分是直飞/中转航程（1是直飞，2是中转）
        args[2]测试环境地址
        :return:
        """
        order_query_data = Public.compose_order_query_data(self, purchase_type, data, pay_verify_data)
        self.log.log_info("%s - %s - B2B Export_order_query.log" % (args[0], args[1]), "B2BExport_log",
                          "b2b order query export request:  %s" % order_query_data)
        if flag == "domestic":
            order_query_re = requests.post(url=self.url.get_environment_export_url(args[2], "order_query_url", "domestic"),
                                           json=order_query_data)
        else:
            order_query_re = requests.post(url=self.url.get_environment_export_url(args[2], "order_query_url", "overseas"),
                                           json=order_query_data)
        # print("订单查询", order_query_re.text)
        order_query_json = order_query_re.json()
        self.log.log_info("%s - %s - B2B Export_order_query.log" % (args[0], args[1]), "B2BExport_log",
                          "b2b order query export response:  %s" % order_query_json)

    def b2b_export_logic(self, *arg):
        """
        B2B接口主逻辑
        :param arg: arg[0]区分代理/平台采购（"PP","PF"）， arg[1]B2C接口获取实时route数据的请求参数名称（"PP_AC_RT"）
         arg[2] 区分B2B/B2C接口("b2b"/"b2c")， arg[3]区分是直飞/中转航程（1是直飞，2是中转），args[4]测试环境地址(如a:deva)
        :return:
        """
        # try:
        search_route, requests_data = self.search(arg[0], arg[1], arg[2], arg[3], arg[4])
        order_data = self.create_order(search_route, requests_data, arg[1], arg[3], arg[4])
        pay_verify = self.pay_verify(order_data, requests_data, arg[1], arg[3], arg[4])
        self.apply_ticketing(arg[0], requests_data, pay_verify, "domestic", arg[2], arg[1], arg[3], arg[4])
        self.order_query(arg[0], requests_data, pay_verify, "domestic", arg[1], arg[3], arg[4])
        # except Exception as e:
        #     print(e)

if __name__ == "__main__":
    b = B2BExport()
    b.b2b_export_logic("PP", "PP_A_RT", "b2b", 2, "a")
    # b.search("PP", "PP_A_RT", "b2b", 2)