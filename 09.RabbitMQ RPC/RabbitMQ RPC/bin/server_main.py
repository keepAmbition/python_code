from foo.RabbitMQ_server import RPCServer

if __name__ == "__main__":
    rpc_client = RPCServer()
    rpc_client.start()