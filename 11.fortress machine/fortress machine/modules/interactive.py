import socket
import sys
from paramiko.py3compat import u
import redis
import time

# windows does not have termios...
try:
    import termios
    import tty
    has_termios = True
except ImportError:
    has_termios = False


def interactive_shell(chan, user_obj, bind_host_obj, cmd_caches, log_recording):
    """
    判断是win还是linux
    :param chan:
    :param user_obj:
    :param bind_host_obj: 主机
    :param cmd_caches: 命令列表
    :param log_recording: 日志记录
    :return:
    """
    # 判断是否是windows shell
    if has_termios:
        posix_shell(chan, user_obj, bind_host_obj, cmd_caches, log_recording)
    else:
        windows_shell(chan)


def posix_shell(chan, user_obj, bind_host_obj, cmd_caches, log_recording):
    """
    :param chan:
    :param user_obj:
    :param bind_host_obj:
    :param cmd_caches:
    :param log_recording:
    :return:
    """
    import select

    oldtty = termios.tcgetattr(sys.stdin)   # 终端标准输入
    try:
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        chan.settimeout(0.0)
        cmd = ''  # 获取cmd 命令
        tab_key = False
        while True:
            r, w, e = select.select([chan, sys.stdin], [], [])
            if chan in r:
                try:
                    x = u(chan.recv(1024))
                    if tab_key:
                        if x not in ('\x07', '\r\n'):
                            # print('tab:',x)
                            cmd += x
                        tab_key = False
                    if len(x) == 0:
                        sys.stdout.write('\r\n*** EOF\r\n')
                        # test for redis to mysql
                        break
                    sys.stdout.write(x)
                    sys.stdout.flush()
                except socket.timeout:
                    pass
            if sys.stdin in r:
                x = sys.stdin.read(1)
                if '\r' != x:
                    cmd += x
                else:
                    user_record_cmd = user_obj.username + '_user_record'
                    pool = redis.ConnectionPool(host='localhost', port=6379)
                    user_record = [user_obj.id, bind_host_obj.id, 'cmd', cmd,
                                   time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())]
                    r = redis.Redis(connection_pool=pool)
                    r.lpush(user_record_cmd, user_record)
                    cmd = ''
                    # 最后用户退出的时候取出来log_item 列表循环写入数据库
                if '\t' == x:
                    tab_key = True
                if len(x) == 0:
                    break
                chan.send(x)

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)


# thanks to Mike Looijmans for this code
def windows_shell(chan):
    '''

    :param chan:
    :return:
    '''
    import threading

    sys.stdout.write("Line-buffered terminal emulation. Press F6 or ^Z to send EOF.\r\n\r\n")

    def writeall(sock):
        while True:
            data = sock.recv(256)
            if not data:
                sys.stdout.write('\r\n*** EOF ***\r\n\r\n')
                sys.stdout.flush()
                break
            sys.stdout.write(data.decode())
            sys.stdout.flush()

    writer = threading.Thread(target=writeall, args=(chan,))
    writer.start()

    try:
        while True:
            d = sys.stdin.read(1)
            if not d:
                break
            chan.send(d)
    except EOFError:
        # user hit ^Z or F6
        pass