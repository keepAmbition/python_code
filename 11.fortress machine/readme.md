```
## readme##
文件目录结构
├── bin
│   ├── __init__.py
│   └── start.py  # 主程序
├── conf
│   ├── action_registers.py  # 程序命令交互
│   ├── __init__.py
│   └── settings.py  # 配置文件
├── log
│   └── __init__.py
├── models
│   ├── __init__.py
│   ├── models.py  # 数据库表模块
├── modules
│   ├── actions.py  # 欢迎页和程序命令交互
│   ├── common_filters.py  # 堡垒机用户主机绑定交互
│   ├── db_conn.py  # mysql连接交互
│   ├── __init__.py
│   ├── interactive.py  # ssh传输命令和命令写入交互
│   ├── ssh_login.py  # ssh连接交互
│   ├── utils.py  # yaml配置交互
│   └── views.py  # 创建表,表数据创建,查看数据库数据交互
└── share  
    └── examples
        ├── new_bindhosts.yml  # 主机绑定关系配置文件
        ├── new_groups.yml  # 组创建，组关系绑定配置文件
        ├── new_hosts.yml  # 主机配置文件
        ├── new_remoteusers.yml  # 主机用户名密码配置文件
        └── new_user.yml  # 堡垒机用户配置文件
		
```
