from foo.RabbitMQ_client import RPCClient

if __name__ == "__main__":
    rpc_client = RPCClient()
    rpc_client.thread_start()