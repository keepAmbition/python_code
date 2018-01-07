```
## test ##

- case:1 创建原始测试数据

C:\Users\dell\PycharmProjects\untitled\home_work\fortress machine>python3 bin\start.py create_users -f share\examples\new_user.
yml
C:\Users\dell\PycharmProjects\untitled\home_work\fortress machine
root {'password': '123@456'}
sean {'password': 123456}
jack {'password': 123456}
C:\Users\dell\AppData\Roaming\Python\Python36\site-packages\pymysql\cursors.py:166: Warning: (1366, "Incorrect string value: '\
\xD6\\xD0\\xB9\\xFA\\xB1\\xEA...' for column 'VARIABLE_VALUE' at row 480")
  result = self._query(query)





C:\Users\dell\PycharmProjects\untitled\home_work\fortress machine>python3 bin\start.py create_remoteUsers -f share\examples\new
_remoteusers.yml
C:\Users\dell\PycharmProjects\untitled\home_work\fortress machine
user0 {'auth_type': 'ssh-password', 'username': 'root', 'password': 123456}
user1 {'auth_type': 'ssh-password', 'username': 'mysql', 'password': 12345678}
user2 {'auth_type': 'ssh-password', 'username': 'colin', 'password': '123@123'}
user3 {'auth_type': 'ssh-password', 'username': 'web', 'password': 12345678}
user4 {'auth_type': 'ssh-key', 'username': 'root'}
C:\Users\dell\AppData\Roaming\Python\Python36\site-packages\pymysql\cursors.py:166: Warning: (1366, "Incorrect string value: '\
\xD6\\xD0\\xB9\\xFA\\xB1\\xEA...' for column 'VARIABLE_VALUE' at row 480")
  result = self._query(query)




C:\Users\dell\PycharmProjects\untitled\home_work\fortress machine>python3 bin\start.py create_hosts -f share\examples\new_hosts
.yml
C:\Users\dell\PycharmProjects\untitled\home_work\fortress machine
{'server1': {'ip': '101.236.23.237', 'port': 22}, 'server2': {'ip': '192.168.84.67', 'port': 12321}, 'server3': {'ip': '192.168
.84.68', 'port': 12321}}
server1 {'ip': '101.236.23.237', 'port': 22}
server2 {'ip': '192.168.84.67', 'port': 12321}
server3 {'ip': '192.168.84.68', 'port': 12321}
C:\Users\dell\AppData\Roaming\Python\Python36\site-packages\pymysql\cursors.py:166: Warning: (1366, "Incorrect string value: '\
\xD6\\xD0\\xB9\\xFA\\xB1\\xEA...' for column 'VARIABLE_VALUE' at row 480")
  result = self._query(query)




C:\Users\dell\PycharmProjects\untitled\home_work\fortress machine>python3 bin\start.py create_groups -f share\examples\new_grou
ps.yml
C:\Users\dell\PycharmProjects\untitled\home_work\fortress machine
bj_group {'user_profiles': ['sean']}
C:\Users\dell\AppData\Roaming\Python\Python36\site-packages\pymysql\cursors.py:166: Warning: (1366, "Incorrect string value: '\
\xD6\\xD0\\xB9\\xFA\\xB1\\xEA...' for column 'VARIABLE_VALUE' at row 480")
  result = self._query(query)
sh_group {'user_profiles': ['jack']}
db_servers {'user_profiles': ['root']}
web_servers {'user_profiles': ['root']}





C:\Users\dell\PycharmProjects\untitled\home_work\fortress machine>python3 bin\start.py create_bindHosts -f share\examples\new_b
indhosts.yml
C:\Users\dell\PycharmProjects\untitled\home_work\fortress machine
bind1 {'hostname': 'server1', 'remote_users': [{'user0': None, 'username': 'root', 'auth_type': 'ssh-password', 'password': 123
456}], 'groups': ['bj_group'], 'user_profiles': ['sean']}
C:\Users\dell\AppData\Roaming\Python\Python36\site-packages\pymysql\cursors.py:166: Warning: (1366, "Incorrect string value: '\
\xD6\\xD0\\xB9\\xFA\\xB1\\xEA...' for column 'VARIABLE_VALUE' at row 480")
  result = self._query(query)
{'user0': None, 'username': 'root', 'auth_type': 'ssh-password', 'password': 123456}
asdsad ['bj_group']
groups: [bj_group]
groups: [bj_group]
user_profiles: [sean]
bind2 {'hostname': 'server2', 'remote_users': [{'user0': None, 'username': 'root', 'auth_type': 'ssh-password', 'password': 123
456}], 'groups': ['bj_group', 'sh_group'], 'user_profiles': ['sean', 'jack']}
{'user0': None, 'username': 'root', 'auth_type': 'ssh-password', 'password': 123456}
asdsad ['bj_group', 'sh_group']
groups: [bj_group, sh_group]
groups: [bj_group, sh_group]
user_profiles: [sean, jack]
bind3 {'hostname': 'server3', 'remote_users': [{'user0': None, 'username': 'root', 'auth_type': 'ssh-password', 'password': 123
456}], 'groups': ['bj_group', 'sh_group'], 'user_profiles': ['sean', 'jack']}
{'user0': None, 'username': 'root', 'auth_type': 'ssh-password', 'password': 123456}
asdsad ['bj_group', 'sh_group']
groups: [bj_group, sh_group]
groups: [bj_group, sh_group]
user_profiles: [sean, jack]
bind4 {'hostname': 'server2', 'remote_users': [{'user2': None, 'username': 'colin', 'auth_type': 'ssh-password', 'password': '1
23@123'}], 'groups': ['web_servers'], 'user_profiles': ['root']}
{'user2': None, 'username': 'colin', 'auth_type': 'ssh-password', 'password': '123@123'}
asdsad ['web_servers']
groups: [web_servers]
groups: [web_servers]
user_profiles: [root]
bind5 {'hostname': 'server3', 'remote_users': [{'user3': None, 'username': 'web', 'auth_type': 'ssh-password', 'password': 1234
5678}, {'user1': None, 'username': 'mysql', 'auth_type': 'ssh-password', 'password': 12345678}], 'groups': ['web_servers', 'db_
servers'], 'user_profiles': ['root']}
{'user3': None, 'username': 'web', 'auth_type': 'ssh-password', 'password': 12345678}
asdsad ['web_servers', 'db_servers']
groups: [db_servers, web_servers]
groups: [db_servers, web_servers]
user_profiles: [root]
{'user1': None, 'username': 'mysql', 'auth_type': 'ssh-password', 'password': 12345678}
asdsad ['web_servers', 'db_servers']
groups: [db_servers, web_servers]
groups: [db_servers, web_servers]
user_profiles: [root]




C:\Users\dell\PycharmProjects\untitled\home_work\fortress machine>mysql -u root  -p
Enter password: ******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 129
Server version: 5.7.17 MySQL Community Server (GPL)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use fortress
Database changed
mysql> show tables;
+---------------------------+
| Tables_in_fortress        |
+---------------------------+
| audit_log                 |
| bind_host                 |
| bindhost_m2m_hostgroup    |
| host                      |
| host_group                |
| remote_user               |
| user_m2m_bindhost         |
| user_profile              |
| userprofile_m2m_hostgroup |
+---------------------------+
9 rows in set (0.00 sec)

mysql> select * from user_profile
    -> ;
+----+----------+----------+
| id | username | password |
+----+----------+----------+
|  1 | root     | 123@456  |
|  2 | sean     | 123456   |
|  3 | jack     | 123456   |
+----+----------+----------+
3 rows in set (0.00 sec)

mysql> select * from host;
+----+----------+----------------+-------+
| id | hostname | ip             | port  |
+----+----------+----------------+-------+
|  1 | server1  | 101.236.23.237 |    22 |
|  2 | server2  | 192.168.84.67  | 12321 |
|  3 | server3  | 192.168.84.68  | 12321 |
+----+----------+----------------+-------+
3 rows in set (0.00 sec)

mysql> select * from bind_host;
+----+---------+---------------+
| id | host_id | remoteUser_id |
+----+---------+---------------+
|  1 |       1 |             1 |
|  2 |       2 |             1 |
|  4 |       2 |             3 |
|  3 |       3 |             1 |
|  6 |       3 |             2 |
|  5 |       3 |             4 |
+----+---------+---------------+
6 rows in set (0.00 sec)

mysql> select * from user_m2m_bindhost;
+----------------+--------------+
| userProfile_id | bind_host_id |
+----------------+--------------+
|              2 |            1 |
|              2 |            2 |
|              3 |            2 |
|              2 |            3 |
|              3 |            3 |
|              1 |            4 |
|              1 |            5 |
|              1 |            6 |
+----------------+--------------+
8 rows in set (0.00 sec)

mysql>



















- case:2 连接主机输入命令

C:\Users\dell\PycharmProjects\untitled\home_work\fortress machine\bin>python3 start.py start_session
C:\Users\dell\PycharmProjects\untitled\home_work\fortress machine
going to start session
Username:sean
Password:123456
C:\Users\dell\AppData\Roaming\Python\Python36\site-packages\pymysql\cursors.py:166: Warning: (1366, "Incorrect string value: '\
\xD6\\xD0\\xB9\\xFA\\xB1\\xEA...' for column 'VARIABLE_VALUE' at row 480")
  result = self._query(query)

    ------------- Welcome [sean] login TinyServer -------------
    
z.       ungroupped hosts (3)
0.       bj_group (3)
[sean]:0
------ Group: bj_group ------
  0.    root@server1(101.236.23.237)
  1.    root@server2(192.168.84.67)
  2.    root@server3(192.168.84.68)
----------- END -----------
[(b)back, (q)quit, select host to login]:0
host: <host_ip:101.236.23.237 -- remote_user.username:root >
*** Connecting...
*** Caught exception: <class 'AttributeError'>: 'Host' object has no attribute 'ip_addr'
Traceback (most recent call last):
  File "C:\Users\dell\PycharmProjects\untitled\home_work\fortress machine\modules\ssh_login.py", line 29, in ssh_login
    client.connect(bind_host_obj.host.ip_addr,
AttributeError: 'Host' object has no attribute 'ip_addr'

C:\Users\dell\PycharmProjects\untitled\home_work\fortress machine\bin>python3 start.py start_session
C:\Users\dell\PycharmProjects\untitled\home_work\fortress machine
going to start session
Username:sean
Password:123456
C:\Users\dell\AppData\Roaming\Python\Python36\site-packages\pymysql\cursors.py:166: Warning: (1366, "Incorrect string value: '\
\xD6\\xD0\\xB9\\xFA\\xB1\\xEA...' for column 'VARIABLE_VALUE' at row 480")
  result = self._query(query)

    ------------- Welcome [sean] login TinyServer -------------
    
z.       ungroupped hosts (3)
0.       bj_group (3)
[sean]:0
------ Group: bj_group ------
  0.    root@server1(101.236.23.237)
  1.    root@server2(192.168.84.67)
  2.    root@server3(192.168.84.68)
----------- END -----------
[(b)back, (q)quit, select host to login]:0
host: <host_ip:101.236.23.237 -- remote_user.username:root >
*** Connecting...
C:\Python36\lib\site-packages\paramiko\client.py:779: UserWarning: Unknown ssh-rsa host key for 101.236.23.237: b'56149f23a4c79
4ea68e7f169234418bd'
  key.get_name(), hostname, hexlify(key.get_fingerprint()),
<paramiko.Transport at 0xcc249908 (cipher aes128-ctr, 128 bits) (active; 1 open channel(s))>
*** Here we go!

--logs: [<models.models.AuditLog object at 0x000001A6CC618D30>]
*** Caught exception: <class 'NameError'>: name 'termios' is not defined
Traceback (most recent call last):
  File "C:\Users\dell\PycharmProjects\untitled\home_work\fortress machine\modules\ssh_login.py", line 45, in ssh_login
    interactive.interactive_shell(chan,user_obj,bind_host_obj,cmd_caches,log_recording)
  File "C:\Users\dell\PycharmProjects\untitled\home_work\fortress machine\modules\interactive.py", line 20, in interactive_shel
l
    windows_shell(chan,user_obj,bind_host_obj,cmd_caches,log_recording)
  File "C:\Users\dell\PycharmProjects\untitled\home_work\fortress machine\modules\interactive.py", line 26, in windows_shell
    oldtty = termios.tcgetattr(sys.stdin)
NameError: name 'termios' is not defined

C:\Users\dell\PycharmProjects\untitled\home_work\fortress machine\bin>python3 start.py start_session
C:\Users\dell\PycharmProjects\untitled\home_work\fortress machine
going to start session
Username:sean
Password:123456
C:\Users\dell\AppData\Roaming\Python\Python36\site-packages\pymysql\cursors.py:166: Warning: (1366, "Incorrect string value: '\
\xD6\\xD0\\xB9\\xFA\\xB1\\xEA...' for column 'VARIABLE_VALUE' at row 480")
  result = self._query(query)

    ------------- Welcome [sean] login TinyServer -------------
    
z.       ungroupped hosts (3)
0.       bj_group (3)
[sean]:0
------ Group: bj_group ------
  0.    root@server1(101.236.23.237)
  1.    root@server2(192.168.84.67)
  2.    root@server3(192.168.84.68)
----------- END -----------
[(b)back, (q)quit, select host to login]:0
host: <host_ip:101.236.23.237 -- remote_user.username:root >
*** Connecting...
C:\Python36\lib\site-packages\paramiko\client.py:779: UserWarning: Unknown ssh-rsa host key for 101.236.23.237: b'56149f23a4c79
4ea68e7f169234418bd'
  key.get_name(), hostname, hexlify(key.get_fingerprint()),
*** Here we go!

Line-buffered terminal emulation. Press F6 or ^Z to send EOF.

Last login: Sun Jan  7 01:55:20 2018 from 183.12.221.147
[root@hanglu-dev01 ~]# ifconfig
ifconfig
eth0      Link encap:Ethernet  HWaddr 00:22:D9:E9:77:27
          inet addr:172.16.94.167  Bcast:172.16.255.255  Mask:255.255.0.0
          inet6 addr: fe80::222:d9ff:fee9:7727/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:276233414 errors:0 dropped:0 overruns:0 frame:0
          TX packets:435360627 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:167924418207 (156.3 GiB)  TX bytes:46786661592 (43.5 GiB)

eth1      Link encap:Ethernet  HWaddr 00:22:0E:04:4B:02
          inet addr:101.236.23.237  Bcast:101.236.23.255  Mask:255.255.255.0
          inet6 addr: fe80::222:eff:fe04:4b02/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:631146089 errors:0 dropped:0 overruns:0 frame:0
          TX packets:540490620 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:314536957323 (292.9 GiB)  TX bytes:123945154351 (115.4 GiB)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:431072840 errors:0 dropped:0 overruns:0 frame:0
          TX packets:431072840 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:65116474938 (60.6 GiB)  TX bytes:65116474938 (60.6 GiB)

[root@hanglu-dev01 ~]# ps -A
ps -A
   PID TTY          TIME CMD
     1 ?        00:00:40 init
     2 ?        00:00:00 kthreadd
     3 ?        00:01:46 migration/0
     4 ?        00:01:37 ksoftirqd/0
     5 ?        00:00:00 migration/0
     6 ?        00:00:11 watchdog/0
     7 ?        00:01:49 migration/1
     8 ?        00:00:00 migration/1
     9 ?        00:02:00 ksoftirqd/1
    10 ?        00:00:08 watchdog/1
    11 ?        00:01:47 migration/2
    12 ?        00:00:00 migration/2
    13 ?        00:01:45 ksoftirqd/2
    14 ?        00:00:08 watchdog/2
    15 ?        00:01:37 migration/3
    16 ?        00:00:00 migration/3
    17 ?        00:01:19 ksoftirqd/3
    18 ?        00:00:07 watchdog/3
    19 ?        00:06:33 events/0
    20 ?        00:04:10 events/1
    21 ?        00:05:23 events/2
    22 ?        00:07:25 events/3
    23 ?        00:00:00 cgroup
    24 ?        00:00:00 khelper
    25 ?        00:00:00 netns
    26 ?        00:00:00 async/mgr
    27 ?        00:00:00 pm
    28 ?        00:00:16 sync_supers
    29 ?        00:00:21 bdi-default
    30 ?        00:00:00 kintegrityd/0
    31 ?        00:00:00 kintegrityd/1
    32 ?        00:00:00 kintegrityd/2
    33 ?        00:00:00 kintegrityd/3
    34 ?        00:08:29 kblockd/0
    35 ?        00:00:03 kblockd/1
    36 ?        00:00:03 kblockd/2
    37 ?        00:00:03 kblockd/3
    38 ?        00:00:00 kacpid
    39 ?        00:00:00 kacpi_notify
    40 ?        00:00:00 kacpi_hotplug
    41 ?        00:00:00 ata_aux
    42 ?        00:00:00 ata_sff/0
    43 ?        00:00:00 ata_sff/1
    44 ?        00:00:00 ata_sff/2
    45 ?        00:00:00 ata_sff/3
    46 ?        00:00:00 ksuspend_usbd
    47 ?        00:00:00 khubd
    48 ?        00:00:00 kseriod
    49 ?        00:00:00 md/0
    50 ?        00:00:00 md/1
    51 ?        00:00:00 md/2
    52 ?        00:00:00 md/3
    53 ?        00:00:00 md_misc/0
    54 ?        00:00:00 md_misc/1
    55 ?        00:00:00 md_misc/2
    56 ?        00:00:00 md_misc/3
    57 ?        00:00:00 linkwatch
    58 ?        00:01:11 khungtaskd
    59 ?        00:01:23 kswapd0
    60 ?        00:00:00 ksmd
    61 ?        00:04:52 khugepaged
    62 ?        00:00:00 aio/0
    63 ?        00:00:00 aio/1
    64 ?        00:00:00 aio/2
    65 ?        00:00:00 aio/3
    66 ?        00:00:00 crypto/0
    67 ?        00:00:00 crypto/1
    68 ?        00:00:00 crypto/2
    69 ?        00:00:00 crypto/3
    74 ?        00:00:00 kthrotld/0
    75 ?        00:00:00 kthrotld/1
    76 ?        00:00:00 kthrotld/2
    77 ?        00:00:00 kthrotld/3
    79 ?        00:00:00 kpsmoused
    80 ?        00:00:00 usbhid_resumer
   172 ?        00:00:00 scsi_eh_0
   173 ?        00:00:00 scsi_eh_1
   260 ?        00:00:00 virtio-blk
   284 ?        00:04:05 jbd2/vda1-8
   285 ?        00:00:00 ext4-dio-unwrit
   364 ?        00:00:00 udevd
   423 ?        00:00:00 virtio-net
   424 ?        00:00:00 virtio-net
   567 ?        00:00:00 kstriped
   626 ?        00:01:51 kauditd
   645 ?        00:08:35 qemu-ga
   857 ?        00:00:00 dhclient
   917 ?        00:03:46 flush-253:0
   987 ?        00:00:00 dhclient
  1031 ?        00:04:45 auditd
  1056 ?        00:03:08 rsyslogd
  1068 ?        00:00:00 dbus-daemon
  1079 ?        00:00:00 cupsd
  1130 ?        00:01:47 sshd
  1138 ?        00:00:08 ntpd
  1214 ?        00:00:56 master
  1224 ?        00:00:21 qmgr
  1233 ?        00:01:19 crond
  1244 ?        00:00:00 atd
  1257 tty1     00:00:00 mingetty
  1259 tty2     00:00:00 mingetty
  1261 tty3     00:00:00 mingetty
  1263 tty4     00:00:00 mingetty
  1265 tty5     00:00:00 mingetty
  1270 ?        00:00:00 udevd
  1271 ?        00:00:00 udevd
  1272 tty6     00:00:00 mingetty
  4385 ?        00:00:00 catalina.sh
  4387 ?        02:25:16 java
  4587 ?        00:00:00 catalina.sh
  4592 ?        00:44:21 java
  6052 ?        00:00:00 catalina.sh
  6056 ?        00:19:51 java
  8169 ?        00:00:00 catalina.sh
  8173 ?        17:17:24 java
[root@hanglu-dev01 ~]# cd /home
cd /home
[root@hanglu-dev01 home]# ls
ls
chendejie  hanglu-dev01_171031_0428.nmon  nmon_x86          softs
fr         hanglu-dev01_171031_0432.nmon  pay_ftp_bill
fr_ext     nmon                           pay_masapay_bill
[root@hanglu-dev01 home]#
 
```
