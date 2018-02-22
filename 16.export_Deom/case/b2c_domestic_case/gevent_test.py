from foo.B2C_Export_Logic import B2cExport

start = B2cExport()

import gevent
import time
from gevent import monkey

monkey.patch_all()

g_list = []


def pf1():
    start.b2c_direct_flight_logic("PP", "PP_A_OW")


def pf2():
    start.b2c_transfer_flight_logic("PP", "PP_A_RT")


def pf3():
    start.b2c_transfer_flight_logic("PP", "PP_A_OW")


def pf4():
    start.b2c_direct_flight_logic("PP", "PP_AC_OW")


def pf5():
    start.b2c_transfer_flight_logic("PP", "PP_AC_OW")

time_start = time.time()
g_list.append(gevent.spawn(pf1))
g_list.append(gevent.spawn(pf2))
g_list.append(gevent.spawn(pf3))
g_list.append(gevent.spawn(pf4))
g_list.append(gevent.spawn(pf5))

gevent.joinall(g_list)
print("同步cost", time.time() - time_start)  # 程序执行消耗的时间