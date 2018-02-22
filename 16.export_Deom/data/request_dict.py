class RequestData(object):
    def __init__(self):
                            # 代理采购+成人+单程直飞/中转请求参数参数
        self.request_data = {"PP_A_OW": {},
                             # 代理采购+成人+往返直飞/中转请求参数参数
                             "PP_A_RT": {},

                             # 代理采购+成人+儿童+单程直飞/中转请求参数参数
                             "PP_AC_OW": {},

                             # 代理采购+成人+儿童+往返直飞/中转请求参数参数
                             "PP_AC_RT": {}}
        self.B2B_request_data = {}

    def get_request_data(self, purchase, request_name, flight_type):
        """
        根据传入参数，返回指定采购商类型的请求参数
        :param purchase: 采购商类型
        :param request_name: 请求参数名称
        :return:请求参数
        """
        if flight_type == 1:
            if purchase == "PF":
                self.request_data[request_name]["cid"] = ""  # JTG、BRY、ZTP
                return self.request_data[request_name]
            else:
                return self.request_data[request_name]
        else:
            self.request_data[request_name]["flightType"] = 2
            if purchase == "PF":
                self.request_data[request_name]["cid"] = ""
                return self.request_data[request_name]
            else:
                return self.request_data[request_name]

    def get_request_data1(self, purchase, request_name):
        """
        根据传入参数，返回指定采购商类型的请求参数
        :param purchase: 采购商类型
        :param request_name: 请求参数名称
        :return:请求参数
        """
        if purchase == "PF":
            self.request_data[request_name]["cid"] = ""
            print(self.request_data[request_name])
            return self.request_data[request_name]
        else:
            return self.request_data[request_name]

    def get_b2b_request_data(self, purchase):
        """
        根据传入参数，返回指定采购商类型的请求参数
        :param purchase: 采购商类型
        :param request_name: 请求参数名称
        :return:请求参数
        """
        if purchase == "PF":
            self.B2B_request_data["cid"] = ""
            print(self.B2B_request_data)
            return self.B2B_request_data
        else:
            return self.B2B_request_data



if __name__ == "__main__":
    r = RequestData()
    a = r.get_request_data("PF", "PP_A_RT")
    print(a)