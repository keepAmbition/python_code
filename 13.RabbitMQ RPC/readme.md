```
Host management(RabbitMQ)/
|-- bin/
|   |-- server_mian.py               #服务端启动主入口
|   |-- client_main.py               #客户端启动主入口
|
|-- conf/
|   |-- settings.py                  #配置
|               
|-- foo/
|   |-- Rabbitmq_server.py           #服务端主逻辑
|   |-- RabbitMQ_client.py           #客户端主逻辑
|
|-- log/
|   |-- log.txt                      #日志
|   |-- log_print.py                 #日志打印函数
|
基于RabbitMQ rpc 的主机管理，可伪异步执行命令,命令如下：
1、run cmd(命令) 通过关键字run运行命令
2、check_task id(result id) 通过关键字check_task id去查看命令执行结果
```
