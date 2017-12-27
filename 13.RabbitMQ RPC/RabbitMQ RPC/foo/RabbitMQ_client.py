import pika
import uuid
import os
import sys
import threading
import random
import time

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from conf import settings
from log.log_print import log_print


class RPCClient(object):
    """
    """

    def __init__(self):
        """
        定义好创建socket实例、声明管道、声明随机产生的唯一queue、消费信息的静态变量
        """
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(settings.RabbitMQ_HOST))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)
        self.result_dict = dict()

    def on_response(self, ch, method, props, body):
        # 当服务端返回的id跟当初请求的id一致时，再去读取服务端发送的信息保持数据的一致性
        if self.corr_id == props.correlation_id:  # 当服务端返回的id跟当初请求的id一致时，保持数据的一致性
           self.response = body

    def call(self, cmd, res_id):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.publish(exchange="",
                             routing_key="rpc_queue",  # 双方的request所用的queue
                             properties=pika.BasicProperties(  # 定义基本属性
                                 reply_to=self.callback_queue,  # 定义客户端服务端双方response的所用的Q
                                 correlation_id=self.corr_id),  # 定义这次request的唯一ID
                             body=cmd)
        while self.response is None:
            self.connection.process_data_events()  # 非 阻塞版的start_consumer()
        self.result_dict.setdefault(str(res_id), self.response.decode())
        return self.result_dict

    def check_task(self, res_id):
        print(self.result_dict[res_id])

    def run(self, cmd):
        if cmd.startswith("run"):
            res_id = random.randint(10000, 99999)
            print("task id:", res_id)
            self.call(cmd.split()[1], res_id)
        elif cmd.startswith("check_task"):
            self.check_task(cmd.split()[1])
        else:
            time.sleep(0.3)
            print("cmd error")

    def thread_start(self):
        while True:
            cmd = input(">>").strip()
            t = threading.Thread(target=self.run, args=(cmd,))
            t.start()


if __name__ == "__main__":
    fibonacci_rpc = RPCClient()
    fibonacci_rpc.thread_start()

