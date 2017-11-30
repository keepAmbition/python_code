import paramiko
import os
import sys
import threading
from stat import S_ISDIR

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from log.log_print import log_print
# from conf.host_dict import HOST_MAP


class FabricHost(object):

    def __init__(self, host, username, password, port=22):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        # cd 切换文件路径后，该变量用于保存实时路径
        self.now_path = ""

    # def show_host(self):
    #     print("目前主机host列表如下:")
    #     for host in HOST_MAP:
    #         #print(HOST_MAP[host]["username"], HOST_MAP[host]["password"]
    #         print(host)
    #     input_host = input("请输入你要操作的主机host,输入多个host时，请用空格隔开：").strip()
    #     for i in input_host.split():
    #         print(len(input_host.split()))
    #         start_host = FabricHost(i, HOST_MAP[i]["username"], HOST_MAP[i]["password"])
    #         self.thread(start_host)

    def connect(self):
        """
        连接远程主机
        :return:FTP SSH 的实例
        """
        t_transport = paramiko.Transport(sock=(self.host, self.port))
        t_transport.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t_transport)
        ssh = paramiko.SSHClient()
        ssh._transport = t_transport
        return sftp, ssh

    def exec_cmd(self, host):
        """
        执行cmd命令函数
        :param host ip地址
        """
        log_print("主机%s已激活" % host)
        self.show_remote_files(host)
        text = """
\n当前路径下目录和文件如上所示，其中目录可执行cd命令，不可执行get or put命令，文件执行get or put命令，exit退出本次主机host操作(如有其他主机host激活，将进入其他主机进行操作)
\n请输入命令：
    1、put 文件名
    2、get 文件名
    3、cd  路径
    4、ls
        """
        print(text)
        while True:
            cmd_list = ["put", "cd", "get", "ls", "exit"]
            cmd = input("cmd>>>").strip()
            if cmd.split()[0] in cmd_list:
                if cmd.startswith("put"):
                    file_name = cmd.split()[1].strip()
                    self.put_file(file_name)
                elif cmd.startswith("get"):
                    file_name = cmd.split()[1]
                    save_file_path = os.path.join(os.path.join(os.path.join(path, "db"), "get_save_file"), file_name)
                    self.get_file(file_name, save_file_path)
                elif cmd.startswith("cd"):
                    self.cd_path(cmd)
                elif cmd == "ls":
                    self.ls_file()
                else:
                    break
            else:
                log_print("cmd is not match")

    def show_remote_now_file(self, new_path):
        """
        判断实时的是目录还是文件
        :param new_path: cd切换后的路径
        """
        sftp, ssh = self.connect()
        cmd = "cd " + new_path + ";pwd"
        std_in, std_out, std_err = ssh.exec_command(cmd)
        dir_files_path = std_out.read().decode().strip()
        # print(dir_files_path)
        # files = list()
        dir_files = sftp.listdir_attr(dir_files_path)
        # print(dir_files)
        for i in dir_files:
            if S_ISDIR(i.st_mode):
                print(i.filename + "（目录）")
            else:
                # files.append(i.filename)
                print(i.filename + "（文件）")

    def show_remote_files(self, host):
        """
        激活远程主机后判断路径下的是目录还是文件
        :param host ip地址
        """
        sftp, ssh = self.connect()
        std_in, std_out, std_err = ssh.exec_command("pwd")
        # 获取当前目录路径
        dir_files_path = std_out.read().decode().strip()
        print("主机%s,当前路径%s下的目录和文件:\n" % (host, dir_files_path))
        dir_files = sftp.listdir_attr(dir_files_path)
        for i in dir_files:
            if S_ISDIR(i.st_mode):
                print(i.filename + "（目录）")
            else:
                print(i.filename + "（文件）")

    def put_file(self, file_name):
        """
        推送文件至远程主机
        :param:file_name 要put的文件名称
        """
        try:
            sftp, ssh = self.connect()
            if self.now_path == "":
                std_in, std_out, std_err = ssh.exec_command("pwd")
                now_path = std_out.read().decode().strip() + "/" + file_name

            else:
                now_path = self.now_path + "/" + file_name
            file_path = os.path.join(os.path.join(os.path.join(path, "db"), "put_file"), file_name)
            sftp.put(file_path, now_path)
            log_print("put successful")
            sftp.close()
        except FileNotFoundError as e:
            log_print(e)

    def get_file(self, file_name, local_path):
        """
        从远程主机下载文件
        :param file_name: 文件名称
        :param local_path: 本地保存get文件的路径
        :return:
        """
        sftp, ssh = self.connect()
        if self.now_path == "":
            std_in, std_out, std_err = ssh.exec_command("pwd")
            now_path = std_out.read().decode().strip()
            '''注释的这行代码也可以用，不过通过os.path.join()组合成的路径，因为Linux系统跟win系统的路径差异,
            下面代码组成的路径就会是这样的: /root\\healthCheck.html,所以想使用下面代码，必须先print(std_out.read().decode().strip())一下
            不然就会找不到文件路径报错'''
            # remote_path = os.path.join(std_out.read().decode().strip(), file_name)
            remote_path = now_path + "/" + file_name
        else:
            remote_path = self.now_path + "/" + file_name
        sftp.get(remote_path, local_path)
        log_print("get successful")
        sftp.close()

    def cd_path(self, cmd):
        """
        根据cd命令切换目录
        :param cmd:命令
        :return:
        """
        ftp, ssh = self.connect()
        # a = cmd + ";pwd;ls"
        try:
            check = ssh.open_sftp()
            check.stat(cmd.split()[1])
            std_in, std_out, std_err = ssh.exec_command(cmd + ";pwd")
            print("目录已切换至:%s" % std_out.read().decode())
            self.now_path = cmd.split()[1].strip()
        except IOError as e:
            log_print(e)

    def ls_file(self):
        """
        展示当前路径下目录和文件
        :return:null
        """
        # ftp, ssh = self.connect()
        if self.now_path == "":
            # std_in, std_out, std_err = ssh.exec_command("ls")
            # print(std_out.read().decode())
            print("路径有没有切换，你ls个啥？")
        else:
            # std_in_one, std_out_one, std_err_one = ssh.exec_command("cd " + self.now_path + ";ls")
            # print(std_out_one.read().decode())
            self.show_remote_now_file(self.now_path)

    def thread(self, f):
        """
        线程函数
        :param f: 类实例
        :return:
        """
        t_obj = []  # 存放子线程实例
        t = threading.Thread(target=f.exec_cmd, args=(self.host,))
        t.start()
        t_obj.append(t)
        for i in t_obj:
            i.join()


if __name__ == "__main__":
    start = FabricHost("101.236.23.237", "root", "8Jy9ZAb3sDsU")
    #start = Fabric("192.168.1.249", "keepambition", "123456")
    #start.get_file('/root/css/flightFooter.css', 'file')
    # start.show_remote_files("cd /home/fr/webServer")
    # start.exec_cmd()
    # start.thread()
    #start.show_host()