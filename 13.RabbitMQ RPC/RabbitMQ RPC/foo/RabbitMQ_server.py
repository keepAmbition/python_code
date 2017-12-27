import pika
import os
import sys

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from conf import settings


class RPCServer(object):
    def __init__(self):
        #创建socket实例，声明管道，声明queue
        self.connect = pika.BlockingConnection(pika.ConnectionParameters(settings.RabbitMQ_HOST))
        self.channel = self.connect.channel()
        self.channel.queue_declare(queue="rpc_queue")

    def execute_cmd(self, cmd):
        result = os.popen(cmd.decode()).read()
        if not result:
            result = "cmd error"
        return result

    def on_request(self, ch, method, props, body):  # props 是客户端发过来的消息
        print("cmd", body.decode())
        response = self.execute_cmd(body)
        # 发布消息
        ch.basic_publish(exchange="",
                         routing_key=props.reply_to,  # props.reply_to从客户端取出双方约定好存放返回结果的queue
                         properties=pika.BasicProperties  # 定义一些基本属性
                         (correlation_id=props.correlation_id),  # props.correlation_id 从客户端取出当前请求的ID返回给客户端做验证
                         body=str(response))
        ch.basic_ack(delivery_tag=method.delivery_tag)  # 手动确认消息被消费

    def start(self):
        self.channel.basic_qos(prefetch_count=1)  # 每次最多处理一个客户端发过来的消息
        # 消费消息
        self.channel.basic_consume(self.on_request,  # 回调函数
                                   queue="rpc_queue")

        print("waiting RPCClient requests")
        self.channel.start_consuming()



if __name__ == "__main__":
    fibonacci_rpc = RPCServer()
    fibonacci_rpc.start()