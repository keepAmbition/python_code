class ExportERL(object):
    def __init__(self):
                            # B2C运价直连接口URL(境内)
        self.export_url = {"b2c_domestic_url": {"search": "",
                                                "verify": "",
                                                "order": "",
                                                "pay_verify": ""},

                           #  B2C运价直连接口URL(境外)
                           "b2c_overseas_url": {"search": "",
                                                "verify": "",
                                                "order": "",
                                                "pay_verify": ""},
                           # B2B运价直连接口URL
                           "b2b_export_url": {"search": "",
                                              "order": "",
                                              "pay_verify": ""},

                           # 申请出票接口URL(domestic境内,overseas境外)
                           "apply_ticketing_url": {"domestic": "",
                                                   "overseas": ""},

                           # 订单信息查询接口URL(domestic境内,overseas境外)
                           "order_query_url": {"domestic": "",
                                               "overseas": ""},

                           # 数据加密URL
                           "encryption_url": {"url": ""},
                           # 数据解密URL
                           "decryption_url": {"url": ""},
                           "b": ""}

    def get_environment_export_url(self, environment, export, url_name):
        """
        根据传入参数名称返回对应测试环境接口的url
        :param environment:测试环境名称
        :param export:接口名称
        :param url_name:接口url
        :return:url
        """
        if environment == "a":
            return self.export_url[export][url_name]
        elif environment == "b":
            pass
        elif environment == "c":
            pass
        elif environment == "d":
            pass
        else:
            pass

    def get_export_url(self, export, url_name):
        """
        根据传入参数名称返回对应加密或解密接口的url
        :param export:接口名称
        :param url_name:接口url
        :return:url
        """
        return self.export_url[export][url_name]

if __name__ == "__main__":
    r = ExportERL()
    a = r.get_export_url("encryption_url", "url")
    print(a)