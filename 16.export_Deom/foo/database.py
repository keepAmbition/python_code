import pymysql
import datetime
import random
import string

from data.conf_dict import ConfData


class ConnectDatabase():
    """
    连接数据库类
    """
    def __init__(self):
        self.conf_data = ConfData()
        self.connection = pymysql.connect(host=self.conf_data.get_conf_data("database")["host"],
                                          port=self.conf_data.get_conf_data("database")["port"],
                                          user=self.conf_data.get_conf_data("database")["user"],
                                          password=self.conf_data.get_conf_data("database")["password"],
                                          db=self.conf_data.get_conf_data("database")["db"],
                                          charset='utf8',
                                          # 以字典形式展示所查询数据
                                          cursorclass=pymysql.cursors.DictCursor)

    def sql_order_status_query(self, order_id):
        """
        根据传入order_id向数据库查询订单的状态
        :param order_id:订单ID
        :return:
        """
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM %s WHERE purchase_order_id = '%s' "
                table_name = self.conf_data.get_conf_data("database")["order_info"]
                data = (table_name, order_id)
                cursor.execute(sql % data)
                result = cursor.fetchone()
                return result["status"]
        finally:
            self.connection.close()

    def change_order_status_to_ticket_completion(self, order_id, *args):
        """
        将订单状态从申请出票更改为出票完成，且贴票号
        :param order_id:采购商订单ID
        :param args:  arg[0] 成人乘客姓名  arg[1] 儿童乘客姓名
        :return:
        """
        try:
            with self.connection.cursor() as cursor:
                # 改变订单状态9 -> 3，保存出票完成时间
                order_info_sql = "UPDATE %s SET status ='%s', ticketing_start_time ='%s'," \
                                 " ticketed_time='%s' WHERE purchase_order_id='%s'"
                order_table_name = self.conf_data.get_conf_data("database")["order_info"]
                date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                data = (order_table_name, 3, date_time, date_time, order_id)
                cursor.execute(order_info_sql % data)
                # self.connection.commit()
                # 回贴票号
                adult_passenger_info_sql = "UPDATE %s SET ticket_num ='%s' WHERE name='%s'"
                passengers_table_name = self.conf_data.get_conf_data("database")["passengers_info"]
                adult_ticket_num = "".join(random.sample(string.ascii_uppercase, 6))
                data = (passengers_table_name, adult_ticket_num, args[0])
                cursor.execute(adult_passenger_info_sql % data)
                if len(args) > 1:
                    child_passenger_info_sql = "UPDATE %s SET ticket_num ='%s' WHERE name='%s'"
                    child_ticket_num = "".join(random.sample(string.ascii_uppercase, 6))
                    data = (passengers_table_name, child_ticket_num, args[1])
                    cursor.execute(child_passenger_info_sql % data)
                self.connection.commit()

        finally:
            self.connection.close()


if __name__ == "__main__":
    b = ConnectDatabase()
    b.change_order_status_to_ticket_completion("3799199020945408", "FCU/DFR", "NXM/BGQ")