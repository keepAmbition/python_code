#_*_coding:utf-8_*_
from modules import views

actions = {
    'start_session': views.start_session,  # 连接server
    'syncdb': views.syncdb,  # 同步数据
    'create_users': views.create_users,  # 创建堡垒机users
    'create_groups': views.create_groups,  # 创建主机组
    'create_hosts': views.create_hosts,  # 创建主机
    'create_bindHosts': views.create_bind_hosts,  # 创建绑定关系
    'create_remoteUsers': views.create_remote_users,  # 创建远程用户
    'view_user_record': views.user_record_cmd  # 查看用户操作命令
}