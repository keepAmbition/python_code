import os
import sys

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)
print(path)

from foo.main_class import FabricHost
from conf.host_dict import HOST_MAP

if __name__ == "__main__":
    print("目前主机host列表如下:")
    for host in HOST_MAP:
        #print(HOST_MAP[host]["username"], HOST_MAP[host]["password"]
        print(host)
    input_host = input("请输入你要操作的主机host,输入多个host时，请用空格隔开：").strip()
    for i in input_host.split():
        start_host = FabricHost(i, HOST_MAP[i]["username"], HOST_MAP[i]["password"])
        start_host.thread(start_host)