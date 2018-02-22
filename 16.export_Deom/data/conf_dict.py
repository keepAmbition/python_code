class ConfData(object):
    def __init__(self):
                        #  成人信息
        self.conf_data = {"adult_dict": {'ageType': '0',
                                         'cardType': 'PP',
                                         'cardIssuePlace': 'CN',
                                         'cardExpired': '20221111',
                                         'nationality': 'CN'},
                          # 儿童信息
                          "child_dict": {'ageType': '1',
                                         'cardType': 'PP',
                                         'cardIssuePlace': 'CN',
                                         'cardExpired': '20211001',
                                         'nationality': 'CN'},
                          # 联系人信息
                          "contact_dict": {'postCode': '00000', 'email': '000000@qq.com'},

                          # 采购信息
                          "pp_cid": "",
                          "pp_key": "",
                          "pf_cid": "",
                          "pf_key": "",

                          "email": {"username": "",
                                    "password": "",
                                    "SMTP_server": "",
                                    "receiver": "",
                                    "sender": "",
                                    "content": """
  hello,

         刚刚在jenkins上运行的接口自动化测试脚本已生成报告和日志，详情请见附件！


                                                                                                      form: QA。

        """},



                          # 数据库信息
                          "database": {"host": "",
                                       "port": 3306,
                                       "user": "root",
                                       "password": "",
                                       "db": "",
                                       "order_info": "",
                                       "passengers_info": ""}}

    def get_conf_data(self, key):
        """
        根据传入的key,返回对应的value数据
        :param key:要取出数据的名称 如："database"，"pf_key"
        :return:
        """
        return self.conf_data[key]


if __name__ == "__main__":
    c = ConfData()
    print(c.get_conf_data("pp_cid"))
